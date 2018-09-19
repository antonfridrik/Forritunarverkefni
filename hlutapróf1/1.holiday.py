month = input("Month: ")
day = input("Day: ")

month = month.capitalize()

if month + " " + day == "January 1": 
    print("New year's day")
elif month + " " + day == "June 17":
    print("National holiday")
elif month + " " + day == "December 25":
    print("Christmas day")