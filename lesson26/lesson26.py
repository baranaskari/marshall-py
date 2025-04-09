# Lesson 26

def if_div(num1, num2):
    return num1 % num2 == 0 
    
def factor_count(num):
    counter = 0 

    for divider in range(1, num+1):
        if if_div(num, divider):
            counter += 1 
    
    return counter 

limit = int(input("enter num"))

for num in range(1, limit+1):
    factor_size = factor_count(num)

    print(f"{num} has {factor_size} factors.")