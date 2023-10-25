from random import randint
import move
import os

x_max = 3
y_max = 10 
player_x = 2
player_y = 1

def map_helyzet(player_x, player_y):
    while True:
        asd = input("Mozog: ")
        if asd == "a" and player_x != 1:
            player_x = move.move_x(-1, player_x)

        elif asd == "d" and player_x != x_max:
            player_x = move.move_x(1, player_x)

        elif asd == "s" and player_y != y_max:
            player_y = move.move_y(1, player_y)
        os.system("cls")

map_helyzet(player_x, player_y)
