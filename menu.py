# importolni - > statok
import random

def fomenu():
    eletero = 10
    energia = 10
    arany = 50
    cukor = 0
    valasztas = 7
    visszaugras = 1
    while visszaugras == 1:
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
                    eloszoregyenesen = 1
                    szokokut = 1
                    print('1 - Balra mész')
                    print('2 - Jobbra mész')
                    print('3 - Egyél édességet (növeld meg az energiaszinted)')
                    print ('4 - Édesség bolt meglátogatása')
                    print ('5 - Kilépés')
                    while valasztas_case_1 >6 or valasztas <1:
                        valasztas_case_1 = int(input('Válassz!'))
                    match valasztas_case_1:
                        case 1:
                            ## Artúr dolga
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
                            pass
                        case 3:
                                edessegeves = int(input('Mennyi édességet szeretnél enni, hogy növeld az energia szinted?'))
                                if edessegeves >= cukor:
                                    print('Nincs elég cukrod. Meglátogatod az édesség boltot?')
                                    print('1 - igen')
                                    print('2 - nem')
                                    meglatogatod_e = int(input('Meglátogatod?'))
                                    match meglatogatod_e:
                                        case 1: 
                                            print('Édesség bolt')
                                            print('1 db cukor: 5 arany')
                                            folytatas = int(input('Kilépsz vagy folytatod? 1 - folytatás ,  0 - kilépés '))
                                            if folytatas == 1:
                                                cukorvalasztas = -1
                                                while cukorvalasztas > 10 or cukorvalasztas < 0:
                                                    cukorvalasztas=int(input('Mennyi cukrot veszel? (egyszerre max 10 db)'))
                                                if arany >= cukorvalasztas*5:
                                                    arany -= cukorvalasztas*5
                                                    cukor += cukorvalasztas
                                                    print(f'Új egyenleged: {arany} db arany')
                                                elif 
                                                else:
                                                    print('Nincs elég aranyad')
                                                    print(f'Jelenlegi egyenleged: {arany} db arany')
                                                    print(f'Szükséged van még {cukorvalasztas*5-arany}')
                                            else:
                                                visszaugras = 1
                                        case 2: 
                                            visszaugras = 1 
                                elif edessegeves <= 0 or edessegeves >=11:
                                    print('Adj meg egy normális mennyiséget!')
                                elif edessegeves > 0 and edessegeves <11:
                                    energia += edessegeves
                                    print(f'Az új energia szinted: {energia}')
                        case 4:
                            print('Édesség bolt')
                            print('1 db cukor: 5 arany')
                            folytatas = int(input('Kilépsz vagy folytatod? 1 - folytatás ,  0 - kilépés '))
                            if folytatas == 1:
                                cukorvalasztas = -1
                                while cukorvalasztas > 10 or cukorvalasztas < 0:
                                    cukorvalasztas=int(input('Mennyi cukrot veszel? (egyszerre max 10 db)'))
                                if arany >= cukorvalasztas*5:
                                    arany -= cukorvalasztas*5
                                    cukor += cukorvalasztas
                                    print(f'Új egyenleged: {arany} db arany')
                                elif 
                                else:
                                    print('Nincs elég aranyad')
                                    print(f'Jelenlegi egyenleged: {arany} db arany')
                                    print(f'Szükséged van még {cukorvalasztas*5-arany}')
                            else:
                                visszaugras = 1
                        case 5:
                            print('Játék vége')

                case 2:
                    eloszorbalra = 1
                        # 3 esemény történhet
                    # z kategóriából 3 féle esemény közül generálódjon 1
                case 4:
                        edessegeves = int(input('Mennyi édességet szeretnél enni, hogy növeld az energia szinted?'))
                        if edessegeves >= cukor:
                            print('Nincs elég cukrod. Meglátogatod az édesség boltot?')
                            print('1 - igen')
                            print('2 - nem')
                            meglatogatod_e = int(input('Meglátogatod?'))
                            match meglatogatod_e:
                                case 1: 
                                    print('Édesség bolt')
                                    print('1 - 1 db cukor (5 arany)')
                                    print('2 - 5 db cukor (25 arany)')
                                    print('3 - 10 db cukor (50 arany)')
                                    print('4 - Édesség bolt elhagyása')
                                    cukorvalasztas = -1
                                    while cukorvalasztas > 10 or cukorvalasztas < 0:
                                        cukorvalasztas=int(input('Mennyi cukrot veszel? (egyszerre max 10 db)'))
                                    if arany >= cukorvalasztas*5:
                                        arany -= cukorvalasztas*5
                                        cukor += cukorvalasztas
                                        print(f'Új egyenleged: {arany} db arany')
                                    else:
                                        print('Nincs elég aranyad')
                                        print(f'Jelenlegi egyenleged: {arany} db arany')
                                        print(f'Szükséged van még {cukorvalasztas*5-arany}')

                                case 2: 
                                    visszaugras = 1 
                        elif edessegeves <= 0 or edessegeves >=11:
                            print('Adj meg egy normális mennyiséget!')
                        elif edessegeves > 0 and edessegeves <11:
                            energia += edessegeves
                            print(f'Az új energia szinted: {energia}')
                            
                case 5:
                    print('Édesség bolt')
                    print('1 - 1 db cukor (5 arany)')
                    print('2 - 5 db cukor (25 arany)')
                    print('3 - 10 db cukor (50 arany)')
                    print('4 - Édesség bolt elhagyása')
                    cukorvalasztas = -1
                    while cukorvalasztas > 10 or cukorvalasztas < 0:
                        cukorvalasztas=int(input('Mennyi cukrot veszel? (egyszerre max 10 db)'))
                    if arany >= cukorvalasztas*5:
                        arany -= cukorvalasztas*5
                        cukor += cukorvalasztas
                        print(f'Új egyenleged: {arany} db arany')
                    else:
                        print('Nincs elég aranyad')
                        print(f'Jelenlegi egyenleged: {arany} db arany')
                        print(f'Szükséged van még {cukorvalasztas*5-arany}')

                case 6:
                    print('Játék vége')

