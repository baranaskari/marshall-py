# Lesson 28

def is_pali(text):
    if not text:
        return True
    elif len(text) < 4:
        return text[0] == text[-1] 
    else:
        mid = len(text) // 2

        for i in range(0, mid):
            left = text[i]
            right = text[-1*i - 1]

            if left != right:
                return False
        return True 

print(is_pali("tacocat"))