# Take marks (0–100) and print the corresponding grade (A/B/C/D/F)

grade = int(input("Enter the grade score: "))

if grade >= 90:
    print("A+")
elif grade >= 80:
    print("A")
elif grade >= 70:
    print("B")
elif grade >= 60:
    print("C")
elif grade >= 50:
    print("D")
else:
    print("F")

