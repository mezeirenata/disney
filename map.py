from random import randint
import move
import os

x_max = 3
y_max = 8 
x = 2
y = 1
def map_generator(x, y):
    for o in range(1, y_max+1):
        print()
        for i in range(1, x_max+1):
            if i == x and o == y:
                print("[x]", end=" ")
            else:
                print("[ ]", end=" ")
map_generator(x, y)


while True:
    asd = input("Mozog: ")
    if asd == "a" and x != 1:
       x = move.move_x(-1, x)

    elif asd == "d" and x != x_max:
        x = move.move_x(1, x)

    elif asd == "s" and y != y_max:
        y = move.move_y(1, y)

    elif asd == "w" and y != 1:
        y = move.move_y(-1, y)
    os.system("cls")
    map_generator(x,y)
    