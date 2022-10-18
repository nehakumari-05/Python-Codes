# Write a Python program to enter your height in cm and convert it into feet and inches. ( 12inches = 1 Foot , 2.54 cm = 1 inch) 
ht = int(input("Enter your height in centimeters: "))
ht_Inch = ht / 2.54;
feet = ht_Inch // 12;
inch = ht_Inch % 12;
print("Your height is", feet, "feet and", inch, "inches")
