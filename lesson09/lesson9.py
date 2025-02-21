# Lesson 9
from random import choice 

invalid = True
player = ''

while invalid:
    player = input("Enter R, P or S: ")

    if player in {'R', 'P', 'S'}:
        invalid = False

cpu = choice(['R', 'P', 'S'])
print(f"CPU: {cpu}") 

if player == cpu:
    print("DRAW!")
else:
    if player == 'R':
        if cpu == 'P':
            print("LOSE!")
        else:
            print("WIN!")
    elif player == 'P':
        if cpu == 'S':
            print("LOSE!")
        else:
            print("WIN!")
    else:
        if cpu == 'R':
            print("LOSE!")
        else:
            print("WIN!")