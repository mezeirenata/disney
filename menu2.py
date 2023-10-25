
import random
from statok import stat,eletero,energia,arany,cukor,player_ATK,player_DEF

def fomenu():
    eletero = 10
    energia = 10
    arany = 50
    cukor = 0
    player_ATK = 2
    player_DEF = 2
    valasztas = 7
    visszaugras = 1
    while visszaugras != 0 and eletero > 0:
        visszaugras = 0
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
                    visszaugras2 = 1
                    while visszaugras2 != 0 and eletero > 0:
                        visszaugras2 = 0
                        print('\n')
                        print('Opciók:')
                        print('1 - Balra mész, a szökőkút körül')
                        print('2 - Jobbra mész, a szökőkút körül')
                        print('3 - Egyél édességet (növeld meg az energiaszinted)')
                        print ('4 - Édesség bolt meglátogatása')
                        print ('5 - Kilépés')
                        print('--------------------------------------------')
                        print('Jelenleg a szökőkútnál tartózkodsz.')
                        print('--------------------------------------------')
                        valasztas_case_1 = int(input('Mit szeretnél csinálni?'))
                        match valasztas_case_1:
                            case 1:
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
                                    mesehos = random.randint(1,3)
                                    if mesehos == 1:
                                        print('Találkoztál Donald kacsával, aki felajánlott neked egy közös képet, ez jó kedvre derített')
                                        eletero += 1
                                    elif mesehos == 2:
                                        print('Találkoztál Shrek-kel. Közölted vele hogy fotózkodni szeretnél vele, de ő csak az összes aranyadért cserébe egyezett bele.')
                                        arany = 0
                                    elif mesehos == 3:
                                        print('Találkoztál Miki egérrel, akitől kértél egy közös képet, azonban ellopta za összes cukrod.')
                                        cukor = 0
                                    stat(eletero,energia,arany,cukor,player_ATK,player_DEF)
                            case 3:
                                    print('--------------------------------------------')
                                    print(f'Energia szinted:{energia}')
                                    edessegeves = int(input('Mennyi édességet szeretnél enni, hogy növeld az energia szinted? (1 cukor -> +1 energia)'))
                                    print('--------------------------------------------')
                                    if edessegeves >= cukor:
                                        print('Nincs elég cukrod. Meglátogatod az édesség boltot?')
                                        print('--------------------------------------------')
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
                                                    print('--------------------------------------------')
                                                    print(f'Vettél {mennyit_veszel} db cukrot. ')
                                                    print(f'Összes cukrod száma: {cukor}')
                                                    print('--------------------------------------------')
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
                                    visszaugras2 = 1
                            case 4:
                                print('--------------------------------------------')
                                print('Édesség bolt')
                                print('1 cukor : 5 arany')
                                print('--------------------------------------------')
                                mennyit_veszel = int(input('Mennyi cukrot szeretnél venni? '))
                                if arany >= mennyit_veszel*5:
                                    arany -= mennyit_veszel*5
                                    cukor += mennyit_veszel
                                    print('--------------------------------------------')
                                    print(f'Vettél {mennyit_veszel} db cukrot. ')
                                    print(f'Összes cukrod száma: {cukor}')
                                    print('--------------------------------------------')
                                else: 
                                    print('Nincs elég aranyad')
                                    print(f'Még {(mennyit_veszel*5) - arany } db aranyra van szükséged.')
                                visszaugras2 = 1
                            case 5:
                                print('Játék vége')
                                

                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    print('Játék vége')
