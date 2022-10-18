""" Write a Python program to convert temperature in degree Celsius to degree
Fahrenheit. If water boils at 100 degree C and freezes as 0 degree C, use the
program to find out what is the boiling point and freezing point of water on
the Fahrenheit scale.
(Hint: T(°F) = T(°C) × 9/5 + 32) """
boil = 100 # boiling point in degree C
freez = 0 # freezing point in degree C 
boilF = boil * (9 / 5) + 32 # boiling point in degree F 
freezF = freez * (9 / 5) + 32 # freezing point in degree F 
print('Boiling point in degree F: ', boilF)
print('Freezing point in degree F: ', freezF)
