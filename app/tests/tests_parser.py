import pytest
from app.utility.second_parser import parse_duration

def test_of_convertion():
    assert parse_duration(0) == "0s"
    assert parse_duration(1) == "1s"
    assert parse_duration(50) == "50s"
    assert parse_duration(60) == "1m"
    assert parse_duration(250) == "4m 10s"
    assert parse_duration(3600) == "1h"
    assert parse_duration(3601) == "1h 1s"
    assert parse_duration(86400) == "1d"
    assert parse_duration(86470) == "1d 1m 10s"


def test_seconds_raises():
    with pytest.raises(ValueError):
        parse_duration(-5)
