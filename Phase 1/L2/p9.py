# Take a day number (1–7) and print the corresponding day name.


day_num = int(input("Enter the day number: "))

match day_num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")            
    case 3:
        print("Wednesday")            
    case 4:
        print("Thrusday")            
    case 5:
        print("Friday")            
    case 6:
        print("Saturday")            
    case _:
        print("Sunday")            
    
