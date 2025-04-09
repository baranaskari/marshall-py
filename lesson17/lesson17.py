# Lesson 17

num = int(input("enter a value: "))

total = 1
multiplier = 1

while multiplier <= num :
    total = total * multiplier 

    multiplier = multiplier +1 

print(f"factorial of {num} is {total}.") 