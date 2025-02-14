# Lesson 4
import math 
section1 = input("Enter section 1 fences:") 
section2 = input("Enter section 2 fences:") 
section3 = input("Enter section 3 fences ") 

can1 = len(section1) 
can2 = len(section2) 
can3 = len(section3) 

total_can = can1 + can2 + can3

cases = math.ceil(total_can / 12) 

leftover = (cases * 12 ) - total_can
price = cases * 14.95 

print(f"Total cans used: {total_can} \n Cans leftover: {leftover} \n Total price: {price}") 