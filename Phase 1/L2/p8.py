# Take an alphabet character and check if it lies between ‘a’ and ‘m’ or ‘n’ and ‘z’

ch = input("Enter the character: ").lower()

if ch in "abcdefghijklm":
    print("Lies in a-m")
else:
    print("Lies in n-z")
    