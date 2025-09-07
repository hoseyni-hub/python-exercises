def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit.
    Formula: (°C × 9/5) + 32 = °F
    """
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit temperature to Celsius.
    Formula: (°F − 32) × 5/9 = °C
    """
    return (fahrenheit - 32) * 5/9


# Example usage:
c = 25
f = 77

print(f"{c}°C is equal to {celsius_to_fahrenheit(c)}°F")
print(f"{f}°F is equal to {fahrenheit_to_celsius(f)}°C")