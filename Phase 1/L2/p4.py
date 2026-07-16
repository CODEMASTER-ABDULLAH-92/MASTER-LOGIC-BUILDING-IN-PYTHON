# Check if one of two given numbers is a multiple of the other.


num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the Second Number: "))

if num1 % num2 == 0 or num2 % num1 == 0:
    print("multiple of Each other:")
