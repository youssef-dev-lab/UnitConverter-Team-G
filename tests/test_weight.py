
import pytest

from converter import convert_weight


def test_kilograms_to_grams():
    assert convert_weight(2, "kg", "g") == pytest.approx(2000)


def test_pounds_to_kilograms():
    assert convert_weight(1, "lb", "kg") == pytest.approx(0.45359237)


def test_grams_to_pounds():
    assert convert_weight(453.59237, "g", "lb") == pytest.approx(1)


def test_unsupported_weight_unit():
    with pytest.raises(ValueError):
        convert_weight(5, "stone", "kg")
