# Lesson 40

def factors_list(num):
    result = []

    for div in range(1, num+1):
        if num % div == 0:
            result.append(div)

    return result 

def prime(num):
    return len(factors_list(num)) == 2 

def prime_list(upper_limit):

    primes = [2]

    if upper_limit == 2:
        return primes
    else:
        for num in range(3, upper_limit, 2):
            if prime(num):
                primes.append(num)

        return primes

print(f"list all primes under 10: {prime_list(10)}")

