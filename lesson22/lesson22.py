# Lesson 22

limit = int(input("enter num"))

fib_0 = 0
fib_1 = 1
fib_n = 0

for n in range(2, limit+1):
    fib_n = fib_1 + fib_0 

    fib_0 = fib_1 
    fib_1 = fin_n 

print(f"fibonacci{limit} is {fib_n}.")