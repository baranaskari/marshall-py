# Lesson 8

counter = 0 

for i in range(6):
    current = input(f"Enter the game {i+1} result: ")

    if current == "W":
        counter += 1

group = 0 
if counter > 4 : 
    group = 1
elif counter > 2 :
    group = 2
elif counter > 0 :
    group = 3

if group == 0: 
    print("Eliminated!") 
    
else:
    print(f"Player is in group {group}.")