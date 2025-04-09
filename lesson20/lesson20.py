# Lesson 20

total = 0

for num in range(1, 10000):

    factor_sum = 0 
    for div in range(1, num):
        if num % div == 0:
            factor_sum += div 

    if factor_sum == num:
        total += num:
        print(f"{num} is a perfect number")

print(f"the total sum of all perfect numbers under 10000 is {total}")