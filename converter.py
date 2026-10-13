
def convert_length(value, from_unit, to_unit):
    """Convert between meters, kilometers, miles, and feet."""
    factors = {
        "m": 1.0,
        "km": 1000.0,
        "mi": 1609.344,
        "ft": 0.3048,
    }

    if from_unit not in factors or to_unit not in factors:
        raise ValueError("Unsupported length unit")

    return value * factors[from_unit] / factors[to_unit]


def convert_temperature(value, from_unit, to_unit):
    """Convert between Celsius, Fahrenheit, and Kelvin."""
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

    return from_celsius[to_unit](to_celsius[from_unit](value))


def convert_weight(value, from_unit, to_unit):
    """Convert between kilograms, grams, and pounds."""
    factors = {
        "kg": 1.0,
        "g": 0.001,
        "lb": 0.45359237,
    }

    if from_unit not in factors or to_unit not in factors:
        raise ValueError("Unsupported weight unit")

    return value * factors[from_unit] / factors[to_unit]
