# Lesson 38

def pali(text):
    return text == text[::-1]

nums = []

for num1 in range(999, 99, -1):
    for num2 in range(999, 99, -1):
        current = num1 + num2

        if pali(str(current)):
            nums.append(current)

print(f"the largest palidrome number in our list is: {max(nums)}")