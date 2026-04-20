
from celsius_to_kelvin import celsius_to_kelvin
from celsius_to_fahrenheit import celsius_to_fahrenheit
from fahrenheit_to_celsius import fahrenheit_to_celsius



def main():
    while True: 
        print("Temperature Converter")
        print("1. Celsius to Kelvin")
        print("2. Celsius to Fahrenheit")
        print("3. Fahrenheit to Celsius")
    
choice = int(input("Enter your choice (1-3): "))
if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    kelvin = celsius_to_kelvin(celsius)
    print(f"{celsius}°C is equal to {kelvin} K")

elif choice == 2:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")

elif choice == 3:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius}°C")

else:
    print("Invalid choice. Please select a number between 1 and 3.")