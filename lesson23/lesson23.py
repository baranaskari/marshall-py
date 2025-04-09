# Lesson 23

loop = True
counter = 0 

while loop:
    user = input("enter the mark or exit to stop inputting marks: ")

    if user.lower().capitalize() == "Exit":
        loop = False 
        break
    else:
        mark = int(user)
        if 0 <= mark <= 100:
            total += mark
            counter += 1
        
        else:
            print("Invalid") 

average = total / counter

print(f"your average: {average}") 