
import pytest
from converter import convert_weight


def test_kilograms_to_grams():
    assert convert_weight(2, "kg", "g") == pytest.approx(2000)


def test_pounds_to_kilograms():
    assert convert_weight(1, "lb", "kg") == pytest.approx(0.45359237)


def test_grams_to_pounds():
    assert convert_weight(453.59237, "g", "lb") == pytest.approx(1)


def test_unsupported_weight_unit():
    with pytest.raises(ValueError, match="Unsupported weight unit"):
        convert_weight(5, "stone", "kg")


def test_weight_rejects_string():
    with pytest.raises(ValueError, match="Value must be a number"):
        convert_weight("abc", "kg", "g")


def test_weight_rejects_boolean():
    with pytest.raises(ValueError, match="Value must be a number"):
        convert_weight(True, "kg", "g")


def test_weight_rejects_nan():
    with pytest.raises(ValueError, match="Value must be finite"):
        convert_weight(float("nan"), "kg", "g")


def test_weight_rejects_infinity():
    with pytest.raises(ValueError, match="Value must be finite"):
        convert_weight(float("inf"), "kg", "g")


def test_zero_weight():
    assert convert_weight(0, "kg", "g") == pytest.approx(0)


def test_negative_weight():
    assert convert_weight(-2, "kg", "g") == pytest.approx(-2000)


def test_same_unit_conversion():
    assert convert_weight(5, "kg", "kg") == pytest.approx(5)

def test_weight_rejects_extremely_large_integer():
    with pytest.raises(ValueError, match="Value must be finite"):
        convert_weight(10**10000, "kg", "g")