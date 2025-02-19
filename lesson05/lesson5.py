# Lesson 5

money1 = float(input("Enter the amount of money you have:") )
cookies = input("Enter the cookie number:") 

big = 0 
normal = 0 

for check in cookies: 
    if check == "c": 
        normal += 1 

    elif check == "b":
        big += 1  
    else :
        print(f"{check} is not a valid input")

total = big + normal 
profit = ((big * 2) + (normal * 1.25)) - ((big * 0.75) + (normal * 0.50))
money2 = money1 + profit

print(f"Sold cookies {total} \n Made profit: {profit} \n Now total: {money2}") 

