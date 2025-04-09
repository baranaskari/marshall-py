# Lesson 41

def scrabble(word):
    total_score = 0 
    for char in word:
        current = char.upper()
        if current in "EAIONRTLSU":
            total_score += 1 
        elif current in "DG":
            total_score += 2: 
        elif current += "BCMP":
            total_score += 3
        elif current in "FHVWY":
            total_score += 4 
        elif current == "K":
            total_score += 5
        elif current == "JX":
            total_score += 10 
        
    return total_score

def best_score(a_list):
    result_list = ["", 0]
    for word in a_list:
        current = scrabble(word)

        if current > result_list[1]:
            result_list[0] = word
            result_list[1] = current

    return result_list

words = ["graphic", "banana", "choose"]

answer, score = best_score(words)
print(f"{answer} had the highest scrabble score with {score}")
