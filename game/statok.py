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

eletero = 10
energia = 10
arany = 50
cukor = 0
player_ATK = 2
player_DEF = 2
szabad = True

def stat(eletero,player_ATK,player_DEF,energia,arany,cukor):

    #while szabad == True:
        
        #os.system('cls')
        if eletero < 3:
            print('╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱') 
        else:
            print('──────────────────────────────────────────────────────────────────────────────────────────')
        #HP
        print(f'HP: {eletero} ', end = ' ')
        for i in range(1, eletero + 1):
            if i % 1 == 0 and eletero > 7:
                prGreen("-")
            elif i % 1 == 0 and eletero <= 7 and eletero > 4:
                prYellow("-")
            elif i % 1 == 0 and eletero <= 4:
                prRed("-")
        if eletero <= 3:
            prRed(" !!! ")
        print()
        #HP
        print(f'\tSebzés: {player_ATK}')
        print(f'\tVédekezés: {player_DEF}')
        #energia
        print(f'Energia: {energia} ', end = ' ')
        for i in range(1, energia + 1):
            if i % 1 == 0 and energia > 7:
                prGreen("-")
            elif i % 1 == 0 and energia <= 7 and energia > 4:
                prYellow("-")
            elif i % 1 == 0 and energia <= 4:
                prRed("-")
        if energia <= 3:
            prRed(" !!! ")
        print()
        #energia
        #tárgyak
        print(f'Pénz: {arany}')
        print(f'Cukorka: {cukor}')


        #tárgyak
        if eletero < 3:
            print('╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱') 
        else:
            print('──────────────────────────────────────────────────────────────────────────────────────────')

stat(eletero,player_ATK,player_DEF,energia,arany,cukor)

