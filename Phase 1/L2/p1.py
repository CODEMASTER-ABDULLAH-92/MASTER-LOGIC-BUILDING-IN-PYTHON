# Take three sides and check if they form a valid triangle


# To form a valid triangle, the Triangle Inequality Theorem must be satisfied.

# The conditions are:

# If the sides are a, b, and c, then:

# a + b > c
# a + c > b
# b + c > a

# These three conditions must all be true.

# Example 1 (Valid Triangle) ✅

# Sides: 3, 4, 5

# 3 + 4 > 5 → 7 > 5 ✅
# 3 + 5 > 4 → 8 > 4 ✅
# 4 + 5 > 3 → 9 > 3 ✅

# Result: Valid Triangle.

# Example 2 (Invalid Triangle) ❌

# Sides: 2, 3, 5

# 2 + 3 > 5 → 5 > 5 ❌ (False)

# Since one condition fails, it is not a valid triangle.


a = int(input("Enter the side1: "))
b = int(input("Enter the side2: "))
c = int(input("Enter the side3: "))

if (a + b > c) and (b + c > a) and (c + a > b):
    print("Valid Triangle: ")
else:
    print("Not a valid Triangle: ")
    
    
# Easy trick to remember:

# The sum of any two sides must always be greater than the third side.