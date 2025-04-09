# Lesson 43

def r_duplicates(a_list):
    result = []

    for value in a_list:
        if value not in result:
            result.append(value)
    return result 

print(r_duplicates([1,2,2,3,4,5,5,5,6,7,7])) 

def unique_letters(a_list):
    result_set = set()
    for word in a_list:
        tmp_set = set(word)
        result_set = result_set | (tmp_set)

    return result_set

test = ["hello", "goodbye", "world", "mr.park!"]
print(unique_letters(test))

def i_count(a_list):
    if a_list:
        result_set = a_list[0] 

        for example_set in a_list[1:]:
            result_set = result_set & example_set 

        return len(result_set)

test = [{1,2,3}, {3,4,5}, {5,6,8}]
print(i_count(test))
