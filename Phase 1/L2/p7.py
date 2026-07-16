# Take two numbers and determine whether both are even, both are odd, or one is
# even and one is odd.

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both are Even")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both are Odd")
elif (num1 % 2 == 0 and num2 % 2 != 0 ) or (num1 % 2 != 0 and num2 % 2 == 0):
    print("Num1 is Even or Odd Num2 is even or odd")




if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both are Even")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both are Odd")
else:
    print("One number is Even and the other is Odd")
    
