from event import event_eldont
from valtozok import *
import random
import time
def dialog_print(arany, player_HP, player_x, player_y):
    event = event_eldont(player_x, player_y)

    match event:
        case 1:
            print('Balra haladtál tovább, és egy sarokba érsz, ahol találkozol Magdi jósnővel, aki behív a sátrába.')
            print('1 - Elfogadod a meghívást')
            print('2 - Elutasítod, és továbbmész')
            bemeszasatorba = 4
            while bemeszasatorba >3 or bemeszasatorba<1:
                bemeszasatorba = int(input('Válassz ! '))
            match bemeszasatorba:
                case 1:
                    print('Elfogadtat a meghívást')
                    atver_vagy_nem = random.randint(1,2)
                    if atver_vagy_nem == 1:
                        arany -= 5
                        print(f'Sajnos nem jártál jól, és Magdi néni átvert. Lenyúlta a pénzed, így vesztettél 5 aranyat.')
                        print(f'Az új egyenleged: {arany} db arany')
                        aranystr = f"a{arany}"
                        return aranystr
                    else:
                        player_HP += 5
                        print(f'Magdi jósnő megjósolta a jövőd. Kiderült hogy a jövőben milliárdos leszel, ezért fülig ér most a mosolyod.(+5 hp)')
                        hpstr = f"h{player_HP}"
                        return hpstr                        
                case 2:
                    print('Elhagyod Magdi néni sátrát, és tovább mész.')

                    elatkoz_vagy_elenged = random.randint(1,2)
                    if elatkoz_vagy_elenged == 1:
                        player_HP -= 5
                        print(f'Magdi jósnéni ezt zokon vette, és elátkozott. (-5hp)')
                        hpstr = f"h{player_HP}"
                        return hpstr
        case 2:
            print("El érkezel egy szökő kúthoz. Jobbra vagy balra kerülöd")
            print("1 - Jobbra")
            print("2 - Balra")
            irany = input("Merre mész?")
            match irany:
                case 1:
                    kedvesvagyelijeszt = random.randint(1,2)
                    if kedvesvagyelijeszt == 1:
                        bohoc = 'kedves volt veled'
                    else:
                        bohoc = 'gonosz volt veled'
                        
                    print(f'Találkozol egy kedves  bohóccal és {bohoc}.')
                    if bohoc == 'kedves volt veled':
                        print('Kaptál 1 db cukrot.')
                        cukor += 1
                    else:
                        print('Vesztettél 1 életerőt .')
                        eletero -= 1
                case 2:
                    print("Egy térre érkezel és 3 figura áll elötted. Gofy, Füles, Hamupipőke.")
                    print("Válassz kivel fótózkodol.")
                    print("1 - Gofy")
                    print("2 - Füles")
                    print("3 - Hamupipőke")
                    valasz = input("Válasz: ")
                    match valasz:
                        case 1:
                            print("Jól érzed magad. (+5 hp).")
                        case 2:
                            print("Fülessel jót beszélgetsz (+20 energia).")
                        case 3: 
                            print("Hamupipőke ad 1 cukorkát neked.")
        case 3:
            print("Megérkezel egy tábla virághoz.")
            print("1 - Közelebb mész.")
            print("2 - Elmész")
            valasz = input("Válasz: ")
            match valasz:
                case 1:
                    virag = random.randint(1,3)
                    match virag:
                        case 1:
                            print("Megüt a virágok szép illata majd mikor közelebb mész annyira elvarázsolódsz hogy észre se veszed hogy egy zsebtolvaj ellopta a cukorkád")
                        case 2:
                            print("A virágoknak már-már bódító illata van és amikor közelebb érsz színte hívogat magához majd elfogyasztod az egyiket öntudatlan állapotban. A virág mérgező volt és egy óra múlva ébredsz fel. vesztettél 5 energiát")
                        case 3:
                            print("A virágoknak már-már bódító illata van megszagolod az egyiket majd hirtelen nagyon jó érzés ragad el és kipihentebbnek és erősebbnek érzed magad. Kaptál 5 energiát")
                    viragsziv = True
                case 2:
                    print("Félsz a virágoktól és inkább nem kockáztatsz (Bölcs döntés) >:( tovább haladsz utadon.")
        case 14:
            if viragsziv == True:
                poni = random.randint(1, 10)
                print("Találkozol egy varázsponival)")
                match poni:
                    case 1:
                        print("Felülsz a póni hátára majd elrepít téged az otthonába és ott egy csodás életet élhetsz. Játék vége.")
                        
                        time.sleep(10)
                        exit()
                    case _:

                        
            else:
                pnvsz = random.randint(1, 2)
                match pnvsz: 
                    case 1:
                        poni
                    case 2:
                        szel
