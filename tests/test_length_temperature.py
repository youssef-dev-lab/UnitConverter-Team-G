
import pytest

from converter import convert_length, convert_temperature


def test_kilometers_to_meters():
    assert convert_length(2, "km", "m") == 2000


def test_miles_to_kilometers():
    assert convert_length(1, "mi", "km") == pytest.approx(1.609344)


def test_unsupported_length_unit():
    with pytest.raises(ValueError):
        convert_length(10, "yards", "m")


def test_celsius_to_fahrenheit():
    assert convert_temperature(0, "C", "F") == pytest.approx(32)


def test_fahrenheit_to_celsius():
    assert convert_temperature(212, "F", "C") == pytest.approx(100)


def test_celsius_to_kelvin():
    assert convert_temperature(0, "C", "K") == pytest.approx(273.15)


def test_unsupported_temperature_unit():
    with pytest.raises(ValueError):
        convert_temperature(20, "X", "C")


def test_length_conversion_same_unit():
    assert convert_length(12, "m", "m") == pytest.approx(12)


def test_temperature_conversion_same_unit():
    assert convert_temperature(25, "C", "C") == pytest.approx(25)

