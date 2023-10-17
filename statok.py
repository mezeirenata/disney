from random import randint
import os

def prRed(skk): print("\033[91m {}\033[00m" .format(skk), end = '')
 
 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk), end = '')
 
 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk), end = '')
 
 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk), end = '')
 
 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk), end = '')
 
 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk), end = '')
 
 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk), end = '')
 
 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk), end = '')

hp = 100
energia = randint(50, 100)
penz = randint(1, 10)
cukorka = randint(1, 10)
player_ATK = 2
player_DEF = 2
szabad = True

def stat(energia, hp, penz, cukorka, player_ATK, player_DEF):

    while szabad == True:
        
        os.system('cls')
        print('---------------------------------------------------------------------------------------')
        #HP
        print(f'HP: {hp} %', end = ' ')
        for i in range(1, hp + 1):
            if i % 10 == 0 and hp > 70:
                prGreen("-")
            elif i % 10 == 0 and hp <= 70 and hp > 40:
                prYellow("-")
            elif i % 10 == 0 and hp <= 40:
                prRed("-")
        if hp <= 30:
            prRed(" !!! ")
        print()
        #HP
        print(f'\tSebzés: {player_ATK}')
        print(f'\tVédekezés: {player_DEF}')
        #energia
        print(f'Energia: {energia} %', end = ' ')
        for i in range(1, energia + 1):
            if i % 10 == 0 and energia > 70:
                prGreen("-")
            elif i % 10 == 0 and energia <= 70 and energia > 40:
                prYellow("-")
            elif i % 10 == 0 and energia <= 40:
                prRed("-")
        if energia <= 30:
            prRed(" !!! ")
        print()
        #energia
        #tárgyak
        print(f'Pénz: {penz}')
        print(f'Cukorka: {cukorka}')


        #tárgyak

        print('---------------------------------------------------------------------------------------')

stat(energia, hp, penz, cukorka, player_ATK, player_DEF)


for i in range(1, hp + 1):
    if i % 10 == 0:
        print('-', end = '')



 
 

