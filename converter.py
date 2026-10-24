"""Validated unit conversion functions for the Unit Converter project."""

import math


def _validate_value(value):
    """Return a finite numeric value, rejecting bools and unsupported types."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Value must be a number")
    try:
        if not math.isfinite(value):
            raise ValueError("Value must be finite")
    except OverflowError:
        raise ValueError("Value must be finite") from None


def _validate_result(result):
    if not math.isfinite(result):
        raise ValueError("Conversion result must be finite")
    return result


def convert_length(value, from_unit, to_unit):
    """Convert between meters, kilometers, miles, and feet."""
    _validate_value(value)
    factors = {"m": 1.0, "km": 1000.0, "mi": 1609.344, "ft": 0.3048}
    if from_unit not in factors or to_unit not in factors:
        raise ValueError("Unsupported length unit")
    return _validate_result(value * factors[from_unit] / factors[to_unit])


def convert_temperature(value, from_unit, to_unit):
    """Convert between Celsius, Fahrenheit, and Kelvin."""
    _validate_value(value)
    to_celsius = {
        "C": lambda x: x,
        "F": lambda x: (x - 32) * 5 / 9,
        "K": lambda x: x - 273.15,
    }
    from_celsius = {
        "C": lambda x: x,
        "F": lambda x: x * 9 / 5 + 32,
        "K": lambda x: x + 273.15,
    }
    if from_unit not in to_celsius or to_unit not in from_celsius:
        raise ValueError("Unsupported temperature unit")
    celsius = to_celsius[from_unit](value)
    if celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero")
    return _validate_result(from_celsius[to_unit](celsius))


def convert_weight(value, from_unit, to_unit):
    """Convert between kilograms, grams, and pounds."""
    _validate_value(value)
    factors = {"kg": 1.0, "g": 0.001, "lb": 0.45359237}
    if from_unit not in factors or to_unit not in factors:
        raise ValueError("Unsupported weight unit")
    return _validate_result(value * factors[from_unit] / factors[to_unit])
