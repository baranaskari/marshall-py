# Lesson 11

coordinate = input("Enter a coordinate: ")
coordinate = coordinate.split(' ') 

coordinate = list(map(int, coordinate)) 

x, y = coordinate

print(f"x: {x}, y: {y}")

if x > 0 :
    if y > 0:
        print(f"At point ({x}, {y}) is in Quadrant 1")

    else:
        print(f"At point ({x}, {y}) is in Quadrant 4")

else:
    if y > 0:
        print(f"At point ({x}, {y}) is in Quadrant 2")

    else:
        print(f"At point ({x}, {y}) is in Quadrant 3")



