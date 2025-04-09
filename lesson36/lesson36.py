# Lesson 36

def factors(num):

    result = []
    for div in range(1, num+1):
        if num % div == 0 : 
            result.append(div) 

    return result

def prime(num):

    return len(factors(num)) == 2

print(f"factors of 20: {factors(20)}")
print(f"is 3 prime: {prime(3)}")
