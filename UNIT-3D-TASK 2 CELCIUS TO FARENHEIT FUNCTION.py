# UNIT-3D-TASK 2 CELCIUS TO FARENHEIT(FUNCTION)
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit
celsius = 37
fahrenheit = celsius_to_fahrenheit(celsius)
print("Fahrenheit:", fahrenheit)