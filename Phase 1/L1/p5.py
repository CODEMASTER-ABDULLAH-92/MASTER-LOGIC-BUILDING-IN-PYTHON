# Check if a given year is a leap year

# A leap year follows these rules:

# If the year is divisible by 400 → ✅ Leap year
# Else if the year is divisible by 100 → ❌ Not a leap year
# Else if the year is divisible by 4 → ✅ Leap year
# Otherwise → ❌ Not a leap year


leapYear = int(input("Enter the year: "))

if leapYear % 400 == 0:
    print("Leap Year: ")
elif leapYear % 100 != 0 and leapYear % 4 == 0:
    print("Leap Year")
else:
    print("Not a leap Year")


# Divisible by 4 and 400 and not by 100
