# Temperature Converter: Celsius ↔ Fahrenheit ↔ Kelvin

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

print("🌡️ Temperature Converter 🌡️")
print("Choose conversion:")
print("1. Celsius → Fahrenheit")
print("2. Fahrenheit → Celsius")
print("3. Celsius → Kelvin")
print("4. Kelvin → Celsius")
print("5. Fahrenheit → Kelvin")
print("6. Kelvin → Fahrenheit")

choice = int(input("Enter your choice (1-6): "))
value = float(input("Enter the temperature value: "))

if choice == 1:
    print(f"{value}°C = {celsius_to_fahrenheit(value):.2f}°F")
elif choice == 2:
    print(f"{value}°F = {fahrenheit_to_celsius(value):.2f}°C")
elif choice == 3:
    print(f"{value}°C = {celsius_to_kelvin(value):.2f}K")
elif choice == 4:
    print(f"{value}K = {kelvin_to_celsius(value):.2f}°C")
elif choice == 5:
    print(f"{value}°F = {fahrenheit_to_kelvin(value):.2f}K")
elif choice == 6:
    print(f"{value}K = {kelvin_to_fahrenheit(value):.2f}°F")
else:
    print("❌ Invalid choice. Please select between 1-6.")