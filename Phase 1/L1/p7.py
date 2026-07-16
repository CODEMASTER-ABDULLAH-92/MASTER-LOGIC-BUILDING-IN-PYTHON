# Take three numbers and print the largest.

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
num3 = int(input("Enter the num3: "))

# res = lambda num1, num2, num3 : num1 if num2 < num1 > num3 else (num2 if num1 < num2 > num3 else num3)



if num1 > num2 and num1 > num3:
    print("Num1")
elif num2 > num1 and num2 > num3:
    print("Num2")
else:
    print("Num3")

