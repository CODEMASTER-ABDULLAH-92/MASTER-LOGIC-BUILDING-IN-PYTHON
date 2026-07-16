# Take a character and check whether it’s uppercase, lowercase, a digit, or a special
# character.

ch = input("Enter the character: ")

if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print("Uppercase: ")
elif ch in "abcdefghijklmnopqrstuvwxyz":
    print("LowerCase")
elif ch in "0123456789":
    print("Digit")
else:
    print("Special Character:")
    