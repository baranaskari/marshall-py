# Lesson 39

def gcd(num1, num2):

    for div in range(min(num1, num2), 0, -1):
        if num1 % div == 0 and num2 % div == 0:
            return div

    return 1 

print(f"The GCD of 8 and 12: {gcd(8,12)}")
print(f"The GCD of 27 and 1080: {gcd(27,1080)}")
