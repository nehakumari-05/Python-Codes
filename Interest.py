"""Write a Python program to calculate the amount payable if money has been
lent on simple interest. per annum and Time = T years. Then Simple
Interest(SI) = (P x R x T)/ 100. Amount payable = Principal + SI. P, R and T
are given as input to the program. """
P = float(input('Enter the principal: '))
R = float(input('Enter the rate of interest per annum: '))
T = float(input('Enter the time in years: '))
SI = (P * R * T)/100
amt = SI + P
print('Total amount:',amt)
