# Take a month number (1–12) and print the number of days in that month (ignore leap years)


month_num = int(input("Enter the month number: "))

# 30 days hath September,
# April, June, and November.
# All the rest have 31,
# Except February alone,
# Which has 28 days clear,
# And 29 in each leap year."

# 4, 6, 9,11


thirthy_days  = [4,6,9,11]
thirty_one_days = [1,3,5,7,8,10,12]
if month_num in thirthy_days:
    print("30 Days")
elif month_num in thirty_one_days:
    print("31 Days")
else:
    print("28 or 29 Days") 