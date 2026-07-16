# Take the hour of the day (0–23) and print “Good Morning”
# ,
# “Good Afternoon”
# ,
# “Good
# Evening”
# , or “Good Night”

# Good Morning: 5 to 11
# Good Afternoon: 12 to 16
# Good Evening: 17 to 20
# Good Night: 21 to 23 and 0 to 4


hour = int(input("Enter the hour: "))

if hour >= 5 and hour <= 11:
    print("Good Morning: ")
elif hour >= 12 and hour <= 16:
    print("Good Afternoon")
elif hour >= 17 and hour <= 20:
    print("Good Evening: ")
else:
    print("Good Night")
     