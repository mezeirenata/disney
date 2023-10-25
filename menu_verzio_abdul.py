from valtozok import *
import os
import statok
import dialog



def fomenu():
    eletero = 10
    energia = 10
    arany = 50
    cukor = 0
    player_ATK = 2
    player_DEF = 2
    visszaugras = 1
    valasztas = 101001010

    os.system("cls")
    statok.stat(eletero,energia,cukor,arany,player_ATK,player_DEF)
    print ('Opciók: ')
    print ('1 - Menj egyenesen')
    print ('2 - Menj balra')
    print ('3 - Menj jobbra')
    print ('4 - Egyél édességet (növeld meg az energiaszinted)')
    print ('5 - Édesség bolt meglátogatása')
    print ('6 - Kilépés')
    print('--------------------------------------------')
    if valasztas == 1 or valasztas == 2 or valasztas == 3:
        dialog.dialog_print(arany, eletero, player_x, player_y)
    while valasztas >6 or valasztas <1:
            valasztas = int(input('Válassz! '))   
    
fomenu()

#kiír mindent