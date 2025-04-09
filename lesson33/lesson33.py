# Lesson 33
def mean(a_list):
    return sum(a_list) / len(a_list) 

def median(a_list):

    sorted_alist = sorted(a_list)
    middle = len(a_list) // 2 

    if len(a_list) % 2 == 0:
        left = sorted_alist[middle -1]
        right = sorted_alist[middle] 
        return (left+right) / 2 
    else:
        return sorted_alist[middle] 

from random import seed
from random import randrange 

seed(1)
data = [randrange(1, 100) for _ in range(randrange(10,30))]
print(f"Our random data {data}")
print(f"mean of data: {mean(data)} and median of dataset {median(data)} ")