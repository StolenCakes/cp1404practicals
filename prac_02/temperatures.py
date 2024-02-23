"""
CP1404/CP5632 - Practical
Program for temperature conversion

Use 2 functions (NOT one!) for converting Celsius to Fahrenheit and vice versa.
Important: Remember SRP - functions should do one thing, so these should be simple calculation functions.
Do not get user input or print output in the functions - do those things outside.
"""
CELSIUS_MODIFIER = 33.8  # value of 9.0 / 5 + 32

def main():
    menu()
    choice = get_choice()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            result = celsius_to_fahrenheit(celsius)
            print(f"Result: {result:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            result = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {result:.2f} C")
        else:
            print("Invalid option.")
        menu()
        choice = get_choice()
    print("Thank you.")

def menu():
    """Function docstring"""
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return celsius * CELSIUS_MODIFIER

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return 5 / 9.0 * (fahrenheit - 32)

def get_choice():
    """Get menu choice"""
    return input(">>> ").upper()

main()
