"""Tests for build_ssh_string() ssh command assembly."""

import csshi
from csshi import Config, Destination


def make_config(**kwargs) -> Config:
    """Return a minimal Config with one destination, overridden by kwargs."""
    dest = kwargs.pop("destination", Destination(host="myhost"))
    kwargs.setdefault("binary", "ssh")
    return Config(destinations=[dest], **kwargs)


class TestBuildSshString:
    def test_minimal(self):
        cfg = make_config()
        assert csshi.build_ssh_string(cfg, 0) == "ssh myhost"

    def test_custom_binary(self):
        cfg = make_config(binary="/usr/local/bin/ssh")
        assert csshi.build_ssh_string(cfg, 0) == "/usr/local/bin/ssh myhost"

    def test_with_user(self):
        cfg = make_config(destination=Destination(host="myhost", user="alice"))
        assert csshi.build_ssh_string(cfg, 0) == "ssh -l alice myhost"

    def test_with_port(self):
        cfg = make_config(destination=Destination(host="myhost", port="2222"))
        assert csshi.build_ssh_string(cfg, 0) == "ssh -p 2222 myhost"

    def test_with_user_and_port(self):
        cfg = make_config(
            destination=Destination(host="myhost", user="alice", port="2222")
        )
        assert csshi.build_ssh_string(cfg, 0) == "ssh -l alice -p 2222 myhost"

    def test_with_jumphost(self):
        cfg = make_config(jumphost="jump.example.com")
        assert csshi.build_ssh_string(cfg, 0) == "ssh -J jump.example.com myhost"

    def test_with_single_option(self):
        cfg = make_config(options=["-i ~/.ssh/id_ansible"])
        assert csshi.build_ssh_string(cfg, 0) == "ssh -i ~/.ssh/id_ansible myhost"

    def test_with_multiple_options(self):
        cfg = make_config(
            options=["-i ~/.ssh/id_ansible", "-o StrictHostKeyChecking=no"]
        )
        result = csshi.build_ssh_string(cfg, 0)
        assert result == "ssh -i ~/.ssh/id_ansible -o StrictHostKeyChecking=no myhost"

    def test_caffeinate_prefix(self):
        cfg = make_config(caffeine=True)
        assert csshi.build_ssh_string(cfg, 0) == "caffeinate -dimsu ssh myhost"

    def test_caffeinate_with_user_and_jumphost(self):
        cfg = make_config(
            caffeine=True,
            jumphost="jump.example.com",
            destination=Destination(host="myhost", user="alice"),
        )
        result = csshi.build_ssh_string(cfg, 0)
        assert result == "caffeinate -dimsu ssh -l alice -J jump.example.com myhost"

    def test_host_is_last_argument(self):
        cfg = make_config(
            destination=Destination(host="target", user="bob", port="22"),
            jumphost="proxy",
            options=["-v"],
        )
        result = csshi.build_ssh_string(cfg, 0)
        assert result.endswith("target")

    def test_second_destination_index(self):
        cfg = Config(
            binary="ssh",
            destinations=[
                Destination(host="host1"),
                Destination(host="host2", user="carol"),
            ],
            options=None,
        )
        assert csshi.build_ssh_string(cfg, 0) == "ssh host1"
        assert csshi.build_ssh_string(cfg, 1) == "ssh -l carol host2"
