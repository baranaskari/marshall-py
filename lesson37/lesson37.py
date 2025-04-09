# Lesson 37

def str_zip(text):
    result = ""
    ctr  = 1 

    for i in range(1, len(text)):
        if text[i] == text[i-1]:
             ctr += 1 

        else: 
            result += text[i-1]
            result += str(ctr) 

            ctr = 1 

    result += text[-1] + str(ctr) 

    if len(result) < len(text):
        return result 
    else: 
        return text 

test =  ["aababbabababaaba", "abcd", "a3ab"]
expected = ["a2bb1c5a3", "abcde", "a"]

for i, test_value in enumerate(test): 
    output = str_zip(test_value)
    print(f"Test {i+1}: ")
    print(f"inputted value: {test_value}")
    print(f"ouputted value: {expected[i]}")
    print(f"Test passed: {output == expected[i]}")
    print("-" * 25)

