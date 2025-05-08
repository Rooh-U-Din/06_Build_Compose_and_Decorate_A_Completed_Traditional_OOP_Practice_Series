# 12. Static Methods

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * 1.8 + 32

celsius = TemperatureConverter.celsius_to_fahrenheit

print(celsius(100))