import random
from statok import stat,eletero,player_ATK,player_DEF,energia,arany,cukor
import os
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

def menu2():
    eletero = 10
    player_ATK = 2
    player_DEF = 2
    energia = 10
    arany = 50
    cukor = 0
    print('\n')
    print('----------------------------------------------------------------------------------------')
    print('Opciók:')
    print('\t 1 - Elfogadod')
    print('\t 2 - Elutasítod')
    print('----------------------------------------------------------------------------------------')
    prPurple('Balra mentél, és egy kisebb séta után találkoztál Magdi jósnénivel.')
    prPurple('Magdi néni behívott a sátrába. Elfogadod?')
    print('----------------------------------------------------------------------------------------')
    energia -= 1
    elfogadod_vagy_nem = 3
    while elfogadod_vagy_nem > 2 or elfogadod_vagy_nem < 1:
        elfogadod_vagy_nem = int(input('Hogyan döntessz?'))
    match elfogadod_vagy_nem:
        case 1:
            energia -= 1
            atver_vagy_nem = random.randint(1,2)
            match atver_vagy_nem:
                case 1:
                    print('\n')
                    print('----------------------------------------------------------------------------------------')
                    prPurple('Elfogadtad a meghívást, azonban nem túl boldogan távoztál a sátrából,')
                    prPurple('mert Magdi néni átvert 15 arannyal. ')
                    print('\t----------')
                    prRed('\t -15 arany')
                    print('\t----------')
                    print('----------------------------------------------------------------------------------------')
                    arany -= 15
                    stat(eletero,player_ATK,player_DEF,energia,arany,cukor) 
                case 2:
                    if eletero < 9:
                        mitkapsz = 1
                    else:
                        mitkapsz = 10-eletero
                    print('\n')
                    print('----------------------------------------------------------------------------------------')
                    prPurple('Elfogadtad a meghívást, és fülig érő mosollyal hagytad el a jóslás után a sátrat,')
                    prPurple('mert remek jövőt jósolt neked Magdi néni')
                    print('\t------')
                    prGreen(f'\t + {mitkapsz}  HP')
                    print('\t------')
                    print('----------------------------------------------------------------------------------------')
                    stat(eletero,player_ATK,player_DEF,energia,arany,cukor) 
        case 2:
            energia -= 1
            elenged_vagy_sem = random.randint(1,2)
            match elenged_vagy_sem:
                case 1:
                    print('\n')
                    print('----------------------------------------------------------------------------------------')
                    prPurple('Elutasítottad Magdi néni meghívását, és szerencsédre most nem haragudott meg rád.')
                    prPurple('Szabadon mehetsz tovább.')
                    print('----------------------------------------------------------------------------------------')
                    stat(eletero,player_ATK,player_DEF,energia,arany,cukor) 
                case 2:
                    print('\n')
                    print('----------------------------------------------------------------------------------------')
                    prPurple('Elutasítottad Magdi néni meghívását, és ő ezt nem hagyta annyiban. ')
                    prPurple('Elátkozott téged.')
                    print('\t-------')
                    prRed('\t - 5 HP')
                    print('\t-------')
                    print('----------------------------------------------------------------------------------------')
                    eletero -= 5
                    stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
    visszaugras = 1
    while visszaugras == 1:
        visszaugras = 0
        print('\n')
        print('----------------------------------------------------------------------------------------')
        print('Opciók:')
        print('\t 1 - Menj tovább')
        print('\t 2 - Egyél édességet (növeld meg az energiaszinted)')
        print ('\t3 - Édesség bolt meglátogatása')
        prRed('\t 4 - Kilépés')
        print('----------------------------------------------------------------------------------------')
        mitszeretnel = 5
        while mitszeretnel > 4 or mitszeretnel < 1:
            mitszeretnel = int(input('Mit szeretnél csinálni? '))
        match mitszeretnel:
            case 1:
                energia -= 1
                elesik_vagy_nem = random.randint(1,2)
                match elesik_vagy_nem:
                    case 1:
                        #elesik
                        print('\n')
                        stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                        print('----------------------------------------------------------------------------------------')
                        print('Opciók:')
                        print('\t 1 - Felsegíted')
                        print('\t 2 - Nem segíted fel')
                        print('----------------------------------------------------------------------------------------')
                        prPurple('Egyenesen mentél tovább Magdi néni sátrától, de mielőtt megközelíthetted volna a szökőkutat az útvégén, ')
                        prPurple('megbotlottál egy kisgyerekben véletlenül, és elesett.')
                        print('----------------------------------------------------------------------------------------')
                        mitteszel = 3
                        while mitteszel > 2 or mitteszel < 1:
                            mitteszel = int(input('Mit teszel?'))
                        match mitteszel:
#TODO                            
                            case 1:
                                pass
                            case 2:
                                pass
                    case 2:
                        #nem esik el, de attól még megbotlottál benne
                        pass
            case 2:
                print('--------------------------------------------')
                print(f'Energia szinted:{energia}')
                edessegeves = int(input('Mennyi édességet szeretnél enni, hogy növeld az energia szinted? (1 cukor -> +1 energia)'))
                print('--------------------------------------------')
                if edessegeves >= cukor:
                    print('\n')
                    print('Nincs elég cukrod. Meglátogatod az édesség boltot?')
                    print('--------------------------------------------')
                    print('\t1 - Igen')
                    print('\t2 - Nem')
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
                                visszaugras = 1
                            else: 
                                print('--------------------------------------------')
                                print('Nincs elég aranyad')
                                print(f'Még {(mennyit_veszel*5) - arany } db aranyra van szükséged.')
                                print('--------------------------------------------')
                                visszaugras = 1
                        case 2: 
                            visszaugras = 1
                elif edessegeves <= 0 or edessegeves > 10-energia:
                    print('Adj meg akkora mennyiséget, hogy ne legyen nagyobb az energiád 10-nél!')
                    visszaugras = 1
                elif edessegeves > 0 and edessegeves <= 10-energia:
                    energia += edessegeves
                    print('--------------------------------------------')
                    print(f'Az új energia szinted: {energia}')
                    print('--------------------------------------------')
                    visszaugras = 1
            case 3:
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
                    visszaugras = 1
                else: 
                    print('\n')
                    print('Nincs elég aranyad')
                    print(f'Még {(mennyit_veszel*5) - arany } db aranyra van szükséged.')
                    visszaugras = 1
            case 4:
                prRed('Kiléptél a játékból')
                break
        
    