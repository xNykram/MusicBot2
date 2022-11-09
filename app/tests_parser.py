import pytest
import second_parser

def test_of_convertion():
    assert second_parser.parse_duration (50) == '50s'
    assert second_parser.parse_duration (250) == '4m 10s'
    assert second_parser.parse_duration (3601) == '1h 1s'
    assert second_parser.parse_duration (86470) == '1d 1m 10s'

def test_seconds_raises():
    with pytest.raises(ValueError):
        second_parser.parse_duration(0)
    with pytest.raises(ValueError):
        second_parser.parse_duration(-5)