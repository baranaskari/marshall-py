# Lesson 31

def anagram(word1, word2):

    if len(word1) != len(word2):
        return False 
    else:
        for char in word1:
            if word1.count(char) != word2.count(char):
                return False
        
        return True

print(anagram("bored", "robed"))
