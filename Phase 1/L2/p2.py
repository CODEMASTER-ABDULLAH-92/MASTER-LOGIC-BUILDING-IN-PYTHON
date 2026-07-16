# If the sides form a valid triangle, determine whether it is equilateral, isosceles, or scalene


# ===========================================
# 1. Equilateral Triangle
# ===========================================

# Condition:

# a == b == c
# All 3 sides are equal.
# Example: 5, 5, 5





# ===========================================
# 2. Isosceles Triangle

# Condition:

# a == b or b == c or a == c
# Exactly 2 sides are equal.
# Examples:
# 5, 5, 3
# 4, 6, 6
# 7, 2, 7

# Note: When writing a program, check for an equilateral triangle first, because an equilateral triangle also satisfies a == b or b == c or a == c.




# ===========================================
# 3. Scalene Triangle
# ===========================================

# Condition:

# a != b and b != c and a != c
# All 3 sides are different.
# Example: 3, 4, 5





num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
num3 = int(input("Enter the num3: "))

if (num1 + num2 > num3) and (num2 + num3 > num1) and (num3 + num1 > num2):
    if num1 == num2 == num3:
        print("Equilateral")
    elif num1 == num2 or num2 == num3 or num3 == num1:
        print("Isosceles")
    elif num1 != num2 and num2 != num3 and num3 != num1:
        print("Scalene")