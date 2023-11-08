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
    os.system("cls")
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
    while valasztas >4 or valasztas <1 :
        valasztas = int(input('Válassz! '))
        if valasztas == 69:
                print('──────────────────────────────────────────────────────────────────────────────────────────')
                prPurple("Találkozol pár varázspónival meg Disney szereplőkkel. Jól beszívtok majd olyan")
                prPurple("tömegsexet nyomtok hogy ihaj meg a csuhaj. Mindenki kifekszik és kibasznak a faszba.")
                prGreen("Vége a játéknak. Easter egg ending.")
                print('──────────────────────────────────────────────────────────────────────────────────────────')
                exit()
    os.system("cls")
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
            case _:
                  prRed("Nem igaz hogy akkora degenerált fasz vagy hogy nem tudsz megnyomni egy 1est vagy 2est vagy 3ast vagy 4est. Hogy a faszba jutottál ide? Csak nem tesztelsz minket?!?!??!?!?!?!??!???! ")
            
main()
 