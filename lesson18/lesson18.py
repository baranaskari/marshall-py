# Lesson 18

num = int(input("enter num: "))

for divider in range(1, num+1):
    print(f"divider variable is {divider}")

    if num % divider == 0:
        print(f"{divider} is factor")
        