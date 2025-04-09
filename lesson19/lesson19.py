# Lesson 19

num = int(input("enter num"))

counter = 0

for div in range(1, num+1):
    if num % div == 0:
        counter +=1 

if counter == 2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not prime") 