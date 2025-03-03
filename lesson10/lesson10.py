# Lesson 10

digits = input("Enter last 4 digits: )")

if digit[0] in {'8', '9'}:
    
    if digit[-1] in {'8', '9'}:
        if digits[1] == digits[2]:
            print(f"The phone number {digits} is a telemarker")

        else:
            print(f"The phone number {digits} is not a telemarker")
    else:
        print(f"The phone number {digits} is not a telemarker")
else:
    print(f"The phone number {digits} is not a telemarker")
