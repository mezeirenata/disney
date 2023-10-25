from random import randint
import move
import os
from valtozok import *

x_max = 3
y_max = 10 

def map_helyzet(player_x, player_y):
    while True:
        asd = valasztas
        if asd == "3" and player_x != 1:
            player_x = move.move_x(-1, player_x)

        elif asd == "2" and player_x != x_max:
            player_x = move.move_x(1, player_x)

        elif asd == "1" and player_y != y_max:
            player_y = move.move_y(1, player_y)
        #os.system("cls")

map_helyzet(player_x, player_y)
