# property is @
class Celsius:
    def __init__(self, temperature=0):
        # self.temperature = temperature
        # assing the temperature the the set fucntion
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError('Temperature below -273 not possible')
        self._temperature = value

# create object of class
man = Celsius()
# assign value to temperature
man.temperature = 6
print(man.temperature)
# call the to_fahrenheit function
print('Degree: ',man.to_fahrenheit())