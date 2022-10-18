# WAP that reads a number of seconds and prints it in form : mins and seconds
totalSecs = int(input("Enter seconds: "))
mins = totalSecs // 60
secs = totalSecs % 60
print(mins, "minutes and", secs, "seconds")
