# Lesson 35

def remove_dup(a_list):
    new_list = []

    for item in a_list:
        if item not in new_list:
            new_list.append(item)

    return new_list

test = ["a", "b", "c", "a", "b", "d"]
print(f"test list: {test}")
print(f"duplicates removed: {remove_dup(test)}")