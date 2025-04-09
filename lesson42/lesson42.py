# Lesson 42

def possible_sum(a_list, target):

    for i, value in enumerate(a_list):
        new_target = target - value 
        if new_target in a_list[i+1:]:
            return True
        
    return False 

test = [1, 3, 5, 12, 22]
target = 12

print(f"can {target} be made from two unique values in: {test}")
print(possible_sum(test, target))