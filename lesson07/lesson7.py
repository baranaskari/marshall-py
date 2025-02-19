# Lesson 7
import random
DC = int(input("Enter a DC level: ")) 
dice = random.randrange(1,21)
print (f"Ability: {dice}") 

if (DC <= 20) :
    if (dice >= DC) : 
        print("Win!") 

    else : 
        print("Lose!") 
else :
    print("DC must be smaller or equal to 20") 
