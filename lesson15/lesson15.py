# Lesson 15

user_input = input("Search for a fruit. ")

fruits = ["Apple", "Banana", "Kiwi"]
found = False 

for fruit in fruits:
    if fruit == user_input:
        print(f"{user_input} is found!")
        found = True 

if not found :
    print(f"{user_input} is not found")  
