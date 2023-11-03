from elsoelagazas import menu1
from masodikelagazas import menu2
from harmadikelagazas import menu3
import os
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
def main():  
    eletero = 10
    player_ATK = 2
    player_DEF = 2
    energia = 10
    arany = 50
    cukor = 0
    valasztas = 7
    visszaugras = 1
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    prPurple('A híres és varázslatos DisneyLand bejáratánál tartózkodsz.')
    prPurple('Célod eljutni a kastélyba, anélkül hogy kirúgnának onnan.')
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    print('Opciók: ')
    print ('\t1 - Menj egyenesen')
    print ('\t2 - Menj balra')
    print ('\t3 - Menj jobbra')
    prRed ('\t4 - Kilépés')
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    print('Mit szeretnél csinálni? ')
    print('──────────────────────────────────────────────────────────────────────────────────────────')
    while valasztas >4 or valasztas <1:
            valasztas = int(input('Válassz! '))
    print('\n')
    match valasztas:
            case 1: 
                    menu1()
            case 2:
                    menu2()
            case 3:
                    menu3()
            case 4:
                    print('\n')
                    prRed('A játéknak vége.')

main()
