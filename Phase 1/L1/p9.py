# Take a character and check if it’s a vowel or consonant.

ch = input("Enter the character: ").lower()

if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print("Vowel")
else:
    print('consonant')
    

#  Pythonic way: 

if ch in 'aeiou':
    print("Vowel")
else:
    print("Consonant")