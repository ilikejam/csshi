"""Tests for set_columns() grid layout calculation."""

import csshi
import pytest


class TestSetColumns:
    def test_square_number_of_sessions(self):
        assert csshi.set_columns(None, None, 4) == 2
        assert csshi.set_columns(None, None, 9) == 3
        assert csshi.set_columns(None, None, 16) == 4

    def test_non_square_uses_floor_sqrt(self):
        assert csshi.set_columns(None, None, 5) == 2
        assert csshi.set_columns(None, None, 6) == 2
        assert csshi.set_columns(None, None, 8) == 2
        assert csshi.set_columns(None, None, 10) == 3

    def test_single_session(self):
        assert csshi.set_columns(None, None, 1) == 1

    def test_columns_arg_used_when_lte_floor_sqrt(self):
        # floor(sqrt(9)) = 3; columns=3 is <= 3
        assert csshi.set_columns(3, None, 9) == 3
        # columns=2 < 3
        assert csshi.set_columns(2, None, 9) == 2
        # columns=1 < 3
        assert csshi.set_columns(1, None, 9) == 1

    def test_columns_arg_ignored_when_gt_floor_sqrt(self):
        # floor(sqrt(4)) = 2; asking for 3 cols is ignored, returns floor_sqrt=2
        assert csshi.set_columns(3, None, 4) == 2

    def test_rows_arg_calculates_columns(self):
        assert csshi.set_columns(None, 2, 6) == 3  # ceil(6/2) = 3
        assert csshi.set_columns(None, 3, 9) == 3  # ceil(9/3) = 3
        assert csshi.set_columns(None, 2, 5) == 3  # ceil(5/2) = 3
        assert csshi.set_columns(None, 1, 5) == 5  # ceil(5/1) = 5

    def test_invalid_columns_raises_system_exit(self):
        with pytest.raises(SystemExit):
            csshi.set_columns(0, None, 4)
        with pytest.raises(SystemExit):
            csshi.set_columns(-1, None, 4)

    def test_invalid_rows_raises_system_exit(self):
        with pytest.raises(SystemExit):
            csshi.set_columns(None, 0, 4)
        with pytest.raises(SystemExit):
            csshi.set_columns(None, -1, 4)
