# Lesson 21

limit = int(input("enter N: "))

max_count = 0
result = 0

for num in range(1, limit+1):
    total = 0 

    for div in range(1, num+1):
        if num % div == 0:
            total += 1 

    if total > max_count:
        max_count = total 
        result = num 

print(f"{result} had the most factors with {max_count} factors.") 