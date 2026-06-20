"""Tests for destination string parsing (host, user, port)."""

import csshi


class TestGetDestinationHost:
    def test_plain_hostname(self):
        assert csshi.get_destination_host("myhost") == "myhost"

    def test_user_at_host(self):
        assert csshi.get_destination_host("alice@myhost") == "myhost"

    def test_host_with_port(self):
        assert csshi.get_destination_host("myhost:22") == "myhost"

    def test_user_at_host_with_port(self):
        assert csshi.get_destination_host("alice@myhost:22") == "myhost"

    def test_ipv6_bare(self):
        assert csshi.get_destination_host("[::1]") == "::1"

    def test_ipv6_with_port(self):
        assert csshi.get_destination_host("[::1]:22") == "::1"

    def test_ipv6_with_user_and_port(self):
        assert csshi.get_destination_host("alice@[::1]:22") == "::1"

    def test_ipv4_address(self):
        assert csshi.get_destination_host("192.168.1.1") == "192.168.1.1"

    def test_ipv4_with_user(self):
        assert csshi.get_destination_host("alice@192.168.1.1") == "192.168.1.1"


class TestGetDestinationUser:
    def test_no_user_no_arg(self):
        assert csshi.get_destination_user("myhost", None) is None

    def test_user_from_arg(self):
        assert csshi.get_destination_user("myhost", "alice") == "alice"

    def test_user_from_destination(self):
        assert csshi.get_destination_user("alice@myhost", None) == "alice"

    def test_destination_user_overrides_arg(self):
        # Destination user takes precedence over -l arg
        assert csshi.get_destination_user("bob@myhost", "alice") == "bob"

    def test_ipv6_with_user(self):
        assert csshi.get_destination_user("alice@[::1]:22", None) == "alice"

    def test_host_with_port_no_user(self):
        assert csshi.get_destination_user("myhost:22", None) is None


class TestGetDestinationPort:
    def test_no_port_no_arg(self):
        assert csshi.get_destination_port("myhost", None) is None

    def test_port_from_arg(self):
        assert csshi.get_destination_port("myhost", "2222") == "2222"

    def test_port_from_host_colon(self):
        assert csshi.get_destination_port("myhost:2222", None) == "2222"

    def test_port_from_user_at_host_colon(self):
        assert csshi.get_destination_port("alice@myhost:2222", None) == "2222"

    def test_ipv6_with_port(self):
        assert csshi.get_destination_port("[::1]:22", None) == "22"

    def test_ipv6_no_port(self):
        # Returns empty string (falsy) when IPv6 address has no port suffix
        result = csshi.get_destination_port("[::1]", None)
        assert result == ""

    def test_ipv6_with_user_and_port(self):
        assert csshi.get_destination_port("alice@[::1]:2222", None) == "2222"

    def test_port_arg_overridden_by_destination_colon(self):
        # Destination port always wins over the -p arg
        assert csshi.get_destination_port("myhost:2222", "22") == "2222"
