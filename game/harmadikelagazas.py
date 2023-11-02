import random
from statok import stat,eletero,player_ATK,player_DEF,energia,arany,cukor
import os
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))

def menu3():
    eletero = 10
    player_ATK = 2
    player_DEF = 2
    energia = 10
    arany = 50
    cukor = 0
    if eletero > 0 and energia > 0:
        pass
    else:
        prRed('Meghaltál, a játéknak vége. ')