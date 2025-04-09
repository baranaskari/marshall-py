# Lesson 32

def duplicate(word1, word2):

    if not word1 or not word2:
        return []
    else:
        set_word1 = set(word1)
        set_word2 = set(word2)

        result = []

        for char in set_word1:
            if char in set_word2:
                result.append(char)

        return sorted(result) 

print(duplicate("hello world", "goodbye world")) 