from mysum.sum.current import MyCurrent, current_in_circle


def test_current_in_circle():
    """Test for calculating current in a circle using Ohm's law."""
    
    radius = 5  # meters
    voltage = 10  # Volts
    resistance = 5  # Ohms
    calculator = MyCurrent()
    result = calculator.calculate_current(radius, voltage, resistance)

    assert result == 2, "Current should be 2 Amps for 10V and 5 Ohms"

def test_current_in_circle_invalid_resistance():
    """Test for invalid resistance input."""
    
    radius = 5  # meters
    voltage = 10  # Volts
    resistance = 0  # Invalid resistance
    calculator = MyCurrent()
    try:
        result = calculator.calculate_current(radius, voltage, resistance)
    except ValueError as e:
        assert str(e) == "Resistance must be positive.", "Error message should be 'Resistance must be positive.'"

def test_current_in_circle_invalid_voltage_or_radius():
    """Test for invalid voltage or radius input."""
    
    radius = -5  # Invalid radius
    voltage = 10  # Volts
    resistance = 5  # Ohms
    calculator = MyCurrent()
    try:
        result = calculator.calculate_current(radius, voltage, resistance)
    except ValueError as e:
        assert str(e) == "Radius and voltage must be positive.", "Error message should be 'Radius and voltage must be positive.'"
    
    radius = 5  # meters
    voltage = -10  # Invalid voltage
    try:
        result = calculator.calculate_current(radius, voltage, resistance)
    except ValueError as e:
        assert str(e) == "Radius and voltage must be positive.", "Error message should be 'Radius and voltage must be positive.'"
