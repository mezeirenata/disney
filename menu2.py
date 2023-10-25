
import random
from statok import stat,eletero,player_ATK,player_DEF,energia,arany,cukor

def fomenu():
    eletero = 10
    player_ATK = 2
    player_DEF = 2
    energia = 10
    arany = 50
    cukor = 0
    valasztas = 7
    visszaugras = 1
    while visszaugras != 0 and eletero > 0:
        visszaugras = 0
        print('Opciók: ')
        print ('\t1 - Menj egyenesen')
        print ('\t2 - Menj balra')
        print ('\t3 - Menj jobbra')
        print ('\t4 - Egyél édességet (növeld meg az energiaszinted)')
        print ('\t5 - Édesség bolt meglátogatása')
        print ('\t6 - Kilépés')
        print('------------------------------------------------------------------')
        print('A híres DisneyLand varázslatos országának bejáratánál tartózkodsz.')
        print('Célod eljutni a kastélyban, anélkül hogy kirúgnának onnan.')
        print('Mit szeretnél csinálni? ')
        print('------------------------------------------------------------------')
        while valasztas >6 or valasztas <1:
                valasztas = int(input('Válassz! '))
        match valasztas:
                case 1: 
                    print('\n')
                    print('---------------------------------------------------')
                    print('Egyenesen mentél tovább.')
                    print('---------------------------------------------------')
                    visszaugras2 = 1
                    while visszaugras2 != 0 and eletero > 0:
                        visszaugras2 = 0
                        energia -= 1
                        print('\n')
                        print('Opciók:')
                        print('\t1 - Balra mész, a szökőkút körül')
                        print('\t2 - Jobbra mész, a szökőkút körül')
                        print('\t3 - Egyél édességet (növeld meg az energiaszinted)')
                        print ('\t4 - Édesség bolt meglátogatása')
                        print ('\t5 - Kilépés')
                        print('---------------------------------------------------')
                        print('Jelenleg a szökőkútnál tartózkodsz.')
                        print('---------------------------------------------------')
                        valasztas_case_1 = 0
                        while valasztas_case_1 < 1 or valasztas_case_1 >5:
                            valasztas_case_1 = int(input('Mit szeretnél csinálni?'))
                        match valasztas_case_1:
                            case 1:
                                print('\n')
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
                                energia -= 1
                                stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                            case 2:
                                    mesehos = random.randint(1,3)
                                    if mesehos == 1:
                                        print('\n')
                                        print('Találkoztál Donald kacsával, aki felajánlott neked egy közös képet, ez jó kedvre derített.')
                                        print('\t-----')
                                        print('\t+ 1hp')
                                        print('\t-----')
                                        if eletero <= 9:
                                            eletero += 1
                                        elif eletero < 10 and eletero >9:
                                            eletero = 10 
                                    elif mesehos == 2:
                                        print('\n')
                                        print('Találkoztál Shrek-kel. Közölted vele hogy fotózkodni szeretnél vele, de ő csak az összes aranyadért cserébe egyezett bele.')
                                        print('\t-------------')
                                        print(f'\t-{arany} arany')
                                        print('\t-------------')
                                        arany = 0
                                    elif mesehos == 3:
                                        print('\n')
                                        print('Találkoztál Miki egérrel, akitől kértél egy közös képet, azonban ellopta az összes cukrod.')
                                        print('\t-------------')
                                        print(f'\t-{cukor} cukor')
                                        print('\t-------------')
                                        cukor = 0
                                    stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                    energia -=1
                            case 3:
                                    print('--------------------------------------------')
                                    print(f'Energia szinted:{energia}')
                                    edessegeves = int(input('Mennyi édességet szeretnél enni, hogy növeld az energia szinted? (1 cukor -> +1 energia)'))
                                    print('--------------------------------------------')
                                    if edessegeves >= cukor:
                                        print('\n')
                                        print('Nincs elég cukrod. Meglátogatod az édesség boltot?')
                                        print('--------------------------------------------')
                                        print('1 - igen')
                                        print('2 - nem')
                                        print('--------------------------------------------')
                                        meglatogatod_e = 0
                                        while meglatogatod_e >2 or meglatogatod_e < 1:
                                            meglatogatod_e = int(input('Meglátogatod?'))
                                        match meglatogatod_e:
                                            case 1: 
                                                print('\n')
                                                print('--------------------------------------------')
                                                print('Édesség bolt')
                                                print('')
                                                print('1 cukor - 5 arany')
                                                print('\n')
                                                print('--------------------------------------------')
                                                print(f'{arany} db aranyad van.')
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
                                        print('Adj meg akkora mennyiséget, hogy ne legyen nagyobb az energiád 10-nél!')
                                    elif edessegeves > 0 and edessegeves <= 10-energia:
                                        energia += edessegeves
                                        print('--------------------------------------------')
                                        print(f'Az új energia szinted: {energia}')
                                        print('--------------------------------------------')
                                    visszaugras2 = 1
                            case 4:
                                print('\n')
                                print('--------------------------------------------')
                                print('Édesség bolt')
                                print('')
                                print('1 cukor - 5 arany')
                                print('\n')
                                print('--------------------------------------------')
                                print(f'{arany} db aranyad van.')
                                mennyit_veszel = int(input('Mennyi cukrot szeretnél venni? '))
                                if arany >= mennyit_veszel*5:
                                    arany -= mennyit_veszel*5
                                    cukor += mennyit_veszel
                                    print('--------------------------------------------')
                                    print(f'Vettél {mennyit_veszel} db cukrot. ')
                                    print(f'Összes cukrod száma: {cukor}')
                                    print('--------------------------------------------')
                                else: 
                                    print('\n')
                                    print('Nincs elég aranyad')
                                    print(f'Még {(mennyit_veszel*5) - arany } db aranyra van szükséged.')
                                visszaugras2 = 1
                            case 5:
                                print('\n')
                                print('Játék vége')
                                break
                    print('\n')
                    print('A szökőkúttól az utad csak egyenesen visz tovább.')
                    tovabbmesz = int(input('\tTovább mész? 1 - igen/ 2 - nem(-> kilépés) ')) 
                    match tovabbmesz:
                        case 1:
                            print('----------------------------------')
                            print('Egyenesen mentél tovább')
                            print('----------------------------------')
                            energia -= 1
                            visszaugras3 = 1
                            while visszaugras3 != 0:
                                visszaugras3 = 0
                                print('\n')
                                print('Opciók:')
                                print('\t1 - Beállsz játszani (legalább 15 arannyal kell rendelkezned)')
                                print('\t2 - Nem állsz be játszani ')
                                print('\t3 - Egyél édességet (növeld meg az energiaszinted)')
                                print ('\t4 - Édesség bolt meglátogatása')
                                print ('\t5 - Kilépés')
                                print('--------------------------------------------')
                                print('Egy szerencsekerék van hozzád közel. ')
                                print('--------------------------------------------')
                                mitteszel = 0
                                while mitteszel >6 or mitteszel < 1:
                                    mitteszel = int(input('Mit teszel?'))
                                match mitteszel:
                                    case 1:
                                        if arany > 0:
                                            szerencsekerek = random.randint(1,3)
                                            match szerencsekerek:
                                                case 1:
                                                    if arany >= 15:
                                                        arany -= 15
                                                    else:
                                                        arany = 0
                                                    print('--------------------------------------------------------------------------------------------------')
                                                    print('Beálltál játszani a szerencsekeréken, azonban nem volt szerencséd és elvesztettél egy kevés pénzt.')
                                                    print('\t-----------')
                                                    print('\t -15 arany ')
                                                    print('\t-----------')
                                                    print('--------------------------------------------------------------------------------------------------')
                                                    stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                                case 2:
                                                    arany = 0
                                                    print('-----------------------------------------------------------------------------')
                                                    print('Beálltál játszani és szerencsétlenséged okán elvesztetted az összes aranyad. ')
                                                    print('-----------------------------------------------------------------------------')
                                                    stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                                case 3:
                                                    arany += 5
                                                    print('-----------------------------------')
                                                    print('Nyertél egy kevés aranyat')
                                                    print('\t----------')
                                                    print('\t +5 arany ')
                                                    print('\t----------')
                                                    print('-----------------------------------')
                                        else:
                                            print('\n')
                                            print('Nincs elég aranyad, hogy játssz')
                                            visszaugras3 = 1
                                    case 2:
                                        print('--------------------------------------------------------------------------------------------------')
                                        print('Mivel úgy döntöttél, hogy kihagyod a szerencsekerekezést, ezért elindultál tovább, azonban megláttál a földön valamit.')
                                        print('Jobban megnézted, és kiderült, hogy 15 arany volt a földön. Ez aztán a szerencse! ')
                                        print('\t-----------')
                                        print('\t +15 arany ')
                                        print('\t-----------')
                                        print('--------------------------------------------------------------------------------------------------')
                                        arany += 15
                                        stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                    case 3:
                                        print('--------------------------------------------')
                                        print(f'Energia szinted:{energia}')
                                        edessegeves = int(input('Mennyi édességet szeretnél enni, hogy növeld az energia szinted? (1 cukor -> +1 energia)'))
                                        print('--------------------------------------------')
                                        if edessegeves >= cukor:
                                            print('\n')
                                            print('Nincs elég cukrod. Meglátogatod az édesség boltot?')
                                            print('--------------------------------------------')
                                            print('\t1 - igen')
                                            print('\t2 - nem')
                                            print('--------------------------------------------')
                                            meglatogatod_e = 0
                                            while meglatogatod_e >2 or meglatogatod_e < 1:
                                                meglatogatod_e = int(input('Meglátogatod?'))
                                            match meglatogatod_e:
                                                case 1: 
                                                    print('\n')
                                                    print('--------------------------------------------')
                                                    print('Édesség bolt')
                                                    print('')
                                                    print('1 cukor - 5 arany')
                                                    print('\n')
                                                    print('--------------------------------------------')
                                                    print(f'{arany} db aranyad van.')
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
                                            print('Adj meg akkora mennyiséget, hogy ne legyen nagyobb az energiád 10-nél!')
                                        elif edessegeves > 0 and edessegeves <= 10-energia:
                                            energia += edessegeves
                                            print('--------------------------------------------')
                                            print(f'Az új energia szinted: {energia}')
                                            print('--------------------------------------------')
                                        visszaugras3 = 1
                                    case 4:
                                        print('\n')
                                        print('--------------------------------------------')
                                        print('Édesség bolt')
                                        print('')
                                        print('1 cukor - 5 arany')
                                        print('\n')
                                        print('--------------------------------------------')
                                        print(f'{arany} db aranyad van.')
                                        mennyit_veszel = int(input('Mennyi cukrot szeretnél venni? '))
                                        if arany >= mennyit_veszel*5:
                                            arany -= mennyit_veszel*5
                                            cukor += mennyit_veszel
                                            print('--------------------------------------------')
                                            print(f'Vettél {mennyit_veszel} db cukrot. ')
                                            print(f'Összes cukrod száma: {cukor}')
                                            print('--------------------------------------------')
                                        else: 
                                            print('\n')
                                            print('Nincs elég aranyad')
                                            print(f'Még {(mennyit_veszel*5) - arany } db aranyra van szükséged.')
                                        visszaugras3 = 1
                                    case 5:
                                        print('\n')
                                        print('Játék vége')
                                        break
                                print('\t 1 - igen')
                                print('\t 2 - nem')
                                folytatas1 = 0
                                while folytatas1 > 2 or folytatas1 < 1:
                                    folytatas1 = int(input('Folytatod a játékot?'))
                                if folytatas1 == 1:
                                    pass
                                else:
                                    print('Játék vége')
                                    break
                        case 2:
                            print('\n')
                            print('Játék vége') 
                            break
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    print('\n')
                    print('Játék vége')
                    break
