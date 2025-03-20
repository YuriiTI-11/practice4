# In mysum/sum/current.py

class MyCurrent:
    """Calculates the current in a segment of a circle."""

    def calculate_current(self, radius: float, voltage: float, resistance: float) -> float:
        """Returns the current in the circle using Ohm's law and basic geometry."""
        if resistance <= 0:
            raise ValueError("Resistance must be positive.")
        if radius <= 0 or voltage <= 0:
            raise ValueError("Radius and voltage must be positive.")
        # Using a simplified formula: I = V / R (Ohm's law)
        return voltage / resistance

def current_in_circle(radius: float, voltage: float, resistance: float):
    """Calculates current in a segment of a circle."""
    calculator = MyCurrent()
    try:
        result = calculator.calculate_current(radius, voltage, resistance)
        print(f"Current in the circle: {result} Amps")
    except ValueError as e:
        print(f"Error: {e}")
