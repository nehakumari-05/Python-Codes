""" Write a program that asks the user to enter their name and age. Print a message addressed to the user that tells the user the year in which they will
turn 100 years old. """
name = input ("Enter the Name: ")
age = int (input("Enter the Age: "))
# Let present year is 2000
user_age = (100 - age) + 2000
print ("The user will in year ", user_age ,"he/she will turn 100 years old.")
