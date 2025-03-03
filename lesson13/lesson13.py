# Lesson 13

month = int(input("Enter the month num: "))
day = int(input("Enter the day num: "))

if month == 2 and day == 18 :
    print("On")
else:
    if month < 2: 
        print("Before")
    elif month > 2 :
        print("After")
    else:
        if day < 18:
            print("Before")
        else:
            print("After")