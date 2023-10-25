# importolni - > statok
import random
from statok import stat
from dialog import dialog_print

def fomenu():
    eletero = 10
    energia = 10
    arany = 50
    cukor = 0
    player_ATK = 2
    player_DEF = 2
    valasztas = 7
    visszaugras = 1
    while visszaugras == 1:
        print('Opciók: ')
        print ('1 - Menj egyenesen')
        print ('2 - Menj balra')
        print ('3 - Menj jobbra')
        print ('4 - Egyél édességet (növeld meg az energiaszinted)')
        print ('5 - Édesség bolt meglátogatása')
        print ('6 - Kilépés')
        while valasztas >6 or valasztas <1:
                valasztas = int(input('Válassz! '))
        match valasztas:
                case 1: 
                    valasztas_case_1 = 7
                    print('\n')
                    print('Opciók:')
                    print('1 - Balra mész, a szökőkút körül')
                    print('2 - Jobbra mész, a szökőkút körül')
                    print('3 - Egyél édességet (növeld meg az energiaszinted)')
                    print ('4 - Édesség bolt meglátogatása')
                    print ('5 - Kilépés')
                    print('--------------------------------------------')
                    print('Megérkeztél a szökőkúthoz.')
                    print('--------------------------------------------')
                    
                    while valasztas_case_1 >6 or valasztas <1:
                        valasztas_case_1 = int(input('Mit szeretnél csinálni?'))
                    match valasztas_case_1:
                        case 1:
                            visszaugras = -1
                            kedvesvagyelijeszt = random.randint(1,2)
                            if kedvesvagyelijeszt == 1:
                                bohoc = 'kedves volt veled'
                            else:
                                bohoc = 'gonosz volt veled'
                            print('--------------------------------------------')
                            print(f'Találkozol egy bohóccal és {bohoc}.')
                            if bohoc == 'kedves volt veled':
                                print('Kaptál 1 db cukrot.')
                                cukor += 1
                            else:
                                print('Vesztettél 1 életerőt .')
                                eletero -= 1
                            print('--------------------------------------------')
                        case 2:
                            print('')
                        case 3:
                                print('--------------------------------------------')
                                print(f'Energia szinted:{energia}')
                                edessegeves = int(input('Mennyi édességet szeretnél enni, hogy növeld az energia szinted? (1 cukor -> +1 energia)'))
                                if edessegeves >= cukor:
                                    print('Nincs elég cukrod. Meglátogatod az édesség boltot?')
                                    print('1 - igen')
                                    print('2 - nem')
                                    print('--------------------------------------------')
                                    meglatogatod_e = int(input('Meglátogatod?'))
                                    match meglatogatod_e:
                                        case 1: 
                                            print('--------------------------------------------')
                                            print('Édesség bolt')
                                            print('1 cukor : 5 arany')
                                            print('--------------------------------------------')
                                            mennyit_veszel = int(input('Mennyi cukrot szeretnél venni? '))
                                            if arany >= mennyit_veszel*5:
                                                arany -= mennyit_veszel*5
                                                cukor += mennyit_veszel
                                                print(f'Vettél {mennyit_veszel} db cukrot. ')
                                                print(f'Összes cukrod száma: {cukor}')
                                            else: 
                                                print('--------------------------------------------')
                                                print('Nincs elég aranyad')
                                                print(f'Még {(mennyit_veszel*5) - arany } db aranyra van szükséged.')
                                                print('--------------------------------------------')
                                        case 2: 
                                             pass
                                elif edessegeves <= 0 or edessegeves > 10-energia:
                                    print('Adj meg egy normális mennyiséget!')
                                elif edessegeves > 0 and edessegeves <= 10-energia:
                                    energia += edessegeves
                                    print('--------------------------------------------')
                                    print(f'Az új energia szinted: {energia}')
                                    print('--------------------------------------------')
                        case 4:
                            print('--------------------------------------------')
                            print('Édesség bolt')
                            print('1 cukor : 5 arany')
                            print('--------------------------------------------')
                            mennyit_veszel = int(input('Mennyi cukrot szeretnél venni? '))
                            if arany >= mennyit_veszel*5:
                                arany -= mennyit_veszel*5
                                cukor += mennyit_veszel
                                print(f'Vettél {mennyit_veszel} db cukrot. ')
                                print(f'Összes cukrod száma: {cukor}')
                            else: 
                                print('Nincs elég aranyad')
                                print(f'Még {(mennyit_veszel*5) - arany } db aranyra van szükséged.')
                        case 5:
                            print('Játék vége')

                case 2:
                    print('\n')
                    print('--------------------------------------------')
                    print('Balra haladtál tovább, és egy sarokba értél.Itt találkozol Magdi jósnővel, aki behív a sátrába.')
                    print('\n')
                    print('1 - Elfogadod a meghívást')
                    print('2 - Elutasítod, és továbbmész')
                    print('--------------------------------------------')
                    bemeszasatorba = 4
                    while bemeszasatorba >3 or bemeszasatorba<1:
                        bemeszasatorba = int(input('Válassz ! '))
                    match bemeszasatorba:
                                case 1:
                                    print('Elfogadtat a meghívást')
########artúr dolga 
                                    atver_vagy_nem = random.randint(1,2)
                                    if atver_vagy_nem == 1:
                                        arany -= 5
                                        print(f'Sajnos nem jártál jól, és Magdi néni átvert. Lenyúlta a pénzed, így vesztettél 5 aranyat.')
                                        print(f'Az új egyenleged: {arany} db arany')
                                    else:
                                        hp += 5
                                        print(f'Magdi jósnő megjósolta a jövőd. Kiderült hogy a jövőben milliárdos leszel, ezért fülig ér most a mosolyod.(+5 hp)')
######artúr dolga vége
                                case 2:
                                    print('Elhagyod Magdi néni sátrát, és tovább mész.')
#####Artúr dolga
                                    elatkoz_vagy_elenged = random.randint(1,2)
                                    if elatkoz_vagy_elenged == 1:
                                        print(f'Magdi jósnéni ezt zokon vette, és elátkozott. (-5hp)')
                                    else:
                                        print('Szerencséd volt. Magdi jósnéni ezúttal elnézte neked, hogy elutasítottad meghívását.')
#####Artúr dolga vége
                    
                case 3:
                    stat(eletero,energia,cukor,arany,player_ATK,player_DEF)
                    visszaugras = -1
                case 4:
                        print('--------------------------------------------')
                        print(f'Energia szinted:{energia}')
                        edessegeves = int(input('Mennyi édességet szeretnél enni, hogy növeld az energia szinted? (1 cukor -> +1 energia)'))
                        if edessegeves >= cukor:
                            print('Nincs elég cukrod. Meglátogatod az édesség boltot?')
                            print('1 - igen')
                            print('2 - nem')
                            print('--------------------------------------------')
                            meglatogatod_e = int(input('Meglátogatod?'))
                            match meglatogatod_e:
                                case 1: 
                                    print('--------------------------------------------')
                                    print('Édesség bolt')
                                    print('1 cukor : 5 arany')
                                    print('--------------------------------------------')
                                    mennyit_veszel = int(input('Mennyi cukrot szeretnél venni? '))
                                    if arany >= mennyit_veszel*5:
                                        arany -= mennyit_veszel*5
                                        cukor += mennyit_veszel
                                        print(f'Vettél {mennyit_veszel} db cukrot. ')
                                        print(f'Összes cukrod száma: {cukor}')
                                    else: 
                                        print('--------------------------------------------')
                                        print('Nincs elég aranyad')
                                        print(f'Még {(mennyit_veszel*5) - arany } db aranyra van szükséged.')
                                        print('--------------------------------------------')
                                case 2: 
                                        pass
                        elif edessegeves <= 0 or edessegeves > 10-energia:
                            print('Adj meg egy normális mennyiséget!')
                        elif edessegeves > 0 and edessegeves <= 10-energia:
                            energia += edessegeves
                            print('--------------------------------------------')
                            print(f'Az új energia szinted: {energia}')
                            print('--------------------------------------------')
                            
                case 5:
                    print('--------------------------------------------')
                    print('Édesség bolt')
                    print('1 cukor : 5 arany')
                    print('--------------------------------------------')
                    mennyit_veszel = int(input('Mennyi cukrot szeretnél venni? '))
                    if arany >= mennyit_veszel*5:
                        arany -= mennyit_veszel*5
                        cukor += mennyit_veszel
                        print(f'Vettél {mennyit_veszel} db cukrot. ')
                        print(f'Összes cukrod száma: {cukor}')
                    else: 
                        print('Nincs elég aranyad')
                        print(f'Még {(mennyit_veszel*5) - arany } db aranyra van szükséged')

                case 6:
                    print('Játék vége')
                    visszaugras = 0
dialog_print()


x= dialog_print()
if "p" in x:
    string = x.removeprefix("p")
    print(f"Pénz: {string}")
elif "h" in x:
    string = x.removeprefix("h")
    print(f"Életerő: {string}")
elif "e" in x:
    string = x.removeprefix("e")
    print(f"Energia: {string}")

