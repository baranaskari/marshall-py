# Lesson 27

def string_cleaner(text): 
    result = ""

    for char in text:
        if char.isalpha():
            result += char.lower()

    return result 

value = string_cleaner("hElLo, woRLD!") 
print(f"value is {value}")