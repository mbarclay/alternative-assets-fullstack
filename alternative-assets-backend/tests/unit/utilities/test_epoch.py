from datetime import datetime

import pytest

from src.utilities.epoch import date_string_to_epoch


def test_date_string_to_epoch_valid_date():
    assert date_string_to_epoch("2000-07-06") == 962841600


def test_date_string_to_epoch_another_valid_date():
    assert date_string_to_epoch("1970-01-01") == 0  # unix epoch start date


def test_date_string_to_epoch_leap_year():
    assert date_string_to_epoch("2000-02-29") == 951782400  # leap year date


def test_date_string_to_epoch_new_century():
    assert date_string_to_epoch("2000-01-01") == 946684800  # start of the 21st century


def test_date_string_to_epoch_far_future_date():
    assert date_string_to_epoch("3000-01-01") == 32503680000  # arbitrary far-future date


def test_date_string_to_epoch_invalid_format():
    with pytest.raises(ValueError):
        date_string_to_epoch("06-07-2000")  # invalid format (dd-mm-yyyy instead of yyyy-mm-dd)


def test_date_string_to_epoch_empty_string():
    with pytest.raises(ValueError):
        date_string_to_epoch("")  # empty string should raise an error


def test_date_string_to_epoch_invalid_date():
    with pytest.raises(ValueError):
        date_string_to_epoch("2000-02-30")  # invalid date (February 30 does not exist)


def test_date_string_to_epoch_invalid_characters():
    with pytest.raises(ValueError):
        date_string_to_epoch("abcd-ef-gh")  # invalid date format and characters
