# Lesson 29

def constant(text, vowel = False):
    ctr = 0

    for char in text:
        char = char.lower()
        if char.isalpha() and char not in {"a", "e", "i", "o" "u"}:
            ctr += 1 

    if not vowel:
        return ctr
    
    else:
        ctr = 0

        for char in text:
            char = char.lower()
            if char.isalpha() and char not in {"a", "e", "i", "o" "u"}:
                ctr += 1 
        return ctr

print(f"the count is {constant("hello, world!"), True}")

