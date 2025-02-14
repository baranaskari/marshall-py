# Lesson 3
import math
side = 0
side = int(side)

while (side == 0):
    user = input("Enter number of equal tiles:") 
    num = float(user)

    if ((num).is_integer()):
        if ((math.sqrt(num)).is_integer()) :
            side = int(math.sqrt(num)) 
            print (f"Side length is {side} ")
    
        else: (print("Enter a number that can be square rooted!") )

    else: 
        print("Please enter a integer") 