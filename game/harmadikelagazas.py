import random
from statok import stat,eletero,player_ATK,player_DEF,energia,arany,cukor
import eventek2
import os
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))

def menu3():
    eletero = 10
    player_ATK = 2
    player_DEF = 2
    energia = 10
    arany = 50
    cukor = 0
    jatekvege = 0
    if eletero > 0 and energia > 0:
###innentől ugyanaz
        if jatekvege != -1:
            print('\n')
            stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
            prPurple('A szökőkúttól az utad csak egyenesen visz tovább.')
            print('---------------')
            print('Opciók:')
            print('\t 1 - Igen')
            prRed('\t 2 - Nem (-> kilépés)')
            print('---------------')
            tovabbmesz = 3
            while tovabbmesz > 2 or tovabbmesz < 1:
                tovabbmesz = int(input('\tTovább mész? ')) 
            match tovabbmesz:
                case 1:
                    print('\n')
                    print('─────────────────────────────────────────────')
                    prPurple('Egyenesen mentél tovább')
                    print('─────────────────────────────────────────────')
                    energia -= 1
                    visszaugras3 = 1
                    while visszaugras3 != 0:
                        visszaugras3 = 0
                        stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                        print('Opciók:')
                        print('\t1 - Beállsz játszani')
                        print('\t2 - Nem állsz be játszani(Tovább mész) ')
                        print('\t3 - Egyél édességet (növeld meg az energiaszinted)')
                        print ('\t4 - Édesség bolt meglátogatása')
                        prRed ('\t5 - Kilépés')
                        print('--------------------------------------------')
                        prPurple('Egy szerencsekerék van hozzád közel. ')
                        print('--------------------------------------------')
                        mitteszel = 0
                        while mitteszel >6 or mitteszel < 1:
                            mitteszel = int(input('Mit teszel? '))
                        match mitteszel:
                            case 1:
                                energia -= 1
                                szerencsekerek = random.randint(1,6)
                                match szerencsekerek:
                                    case 1:
                                        if arany >= 15:
                                            arany -= 15
                                        else:
                                            arany = 0
                                        print('--------------------------------------------------------------------------------------------------')
                                        eventek2.szk1()
                                        print('--------------------------------------------------------------------------------------------------')
                                        stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                    case 2:
                                        print('-----------------------------------------------------------------------------')
                                        eventek2.szk2()
                                        prRed(f'-{arany} arany')
                                        print('-----------------------------------------------------------------------------')
                                        stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                        arany = 0
                                    case 3:
                                        arany += 15
                                        print('-----------------------------------')
                                        eventek2.szk3()
                                        print('-----------------------------------')
                                        stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                    case 4:
                                        arany += 50
                                        print('-----------------------------------')
                                        eventek2.szk4()
                                        print('-----------------------------------')
                                        stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                    case 5:
                                        if arany >= 15:
                                            vesztesz = 15
                                        else:
                                            vesztesz = arany
                                        print('--------------------------------------------------------------------------------------------------')
                                        eventek2.szk5()
                                        print('\t-----------')
                                        prRed(f'\t -{vesztesz} arany ')
                                        print('\t-----------')
                                        print('--------------------------------------------------------------------------------------------------')
                                        stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                    case 6:
                                        print('-----------------------------------')
                                        eventek2.szk6()
                                        print('-----------------------------------')
                                        kastelyjegy = 1
                                        stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                print('\n')
                                print('-------------------------------')
                                print('\t 1 - Igen')
                                print('\t 2 - Nem')
                                print('-------------------------------')
                                folytatas1 = 0
                                while folytatas1 > 2 or folytatas1 < 1:
                                    folytatas1 = int(input('Folytatod a játékot? '))
                                match folytatas1:    
                                    case 1:
                                        stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                        print('\n')
                                        print('Opciók:')
                                        print('\t 1 - Belépsz a kastélyba ')
                                        prRed('\t 2 - Nem lépsz be a kastélyba')
                                        print('-------------------------------------------------------------------------------------')
                                        prPurple('Miután részt vettél a szerencsekerekezésben, megláttad a kastélyt és elindultál felé.')
                                        prPurple('Egy kisebb séta után elérkeztél a kastély bejáratához. ')
                                        print('-------------------------------------------------------------------------------------')
                                        belepsz_vagy_nem = 5
                                        while belepsz_vagy_nem > 2 or belepsz_vagy_nem < 1:
                                            belepsz_vagy_nem = int(input('Hogyan döntesz? '))
                                        energia -= 1
                                        match belepsz_vagy_nem:
                                            case 1:
                                                stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                                if kastelyjegy == 1:
                                                    print('-------------------------------------------------------------------------------------')
                                                    prPurple('Beléptél a kastélyba.')
                                                    prPurple('Mivel volt egy korábbról szerzett jegyed, ezért a kastélyban jegyváráslás nélkül továbbmehetsz.')
                                                    print('-------------------------------------------------------------------------------------')
                                                    print('\n')
                                                    prGreen('Sikeresen kijátszottad a játékot, az utadat szabadon folytathatod a kastélyban!') 
                                                else:
                                                    print('\n')
                                                    print('-------------------------------------------------------------------------------------')
                                                    prPurple('Beléptél a kastélyba, viszont ahhoz hogy beljebb mehess venned kell egy jegyet!')
                                                    print('')
                                                    prPurple('\t1 jegy - 60 arany')
                                                    print('-------------------------------------------------------------------------------------')
                                                    print(f'Az aranyaid száma:{arany}')
                                                    if arany >= 60:
                                                        print('------------------------')
                                                        print('Opciók')
                                                        print('\t 1 - Veszel jegyet')
                                                        print('\t 2 - Nem veszel jegyet')
                                                        print('------------------------')
                                                        veszeljegy = 3
                                                        while veszeljegy > 2 or veszeljegy < 1:
                                                            veszeljegy = int(input('Veszel jegyet? '))
                                                            match veszeljegy:
                                                                case 1:
                                                                    arany -= 60
                                                                    elszakad_vagy_nem = random.randint(1,2)
                                                                    match elszakad_vagy_nem:
                                                                        case 1:
                                                                            print('-------------------------------------')
                                                                            prPurple('Vettél sikeresen egy kastély belépőt.')
                                                                            print('-------------------------------------')
                                                                            print('\n')
                                                                            prGreen('Kijátszottad a játékot, az utadat szabadon folytathatod a kastélyban!') 
                                                                            break
                                                                        case 2:
                                                                            print('-----------------------------------------------------------------------')
                                                                            prPurple('Vettél sikeresen egy kastély belépőt, azonban kiejtetted a kezedből.')
                                                                            prPurple('A jegyet soha nem találtad meg ')
                                                                            print('-----------------------------------------------------------------------')
                                                                            print('\n')
                                                                            prRed('Sajnos a játéknak vége!')
                                                                            break
                                                                case 2:
                                                                    prRed('Az őrök eltávolítottak a kastélyból, a játéknak vége.')
                                                                    break
                                                    else:
                                                        print('----------------------------------------------------------------------------')
                                                        print('Opciók')
                                                        prRed('\t 1 - Mivel nincs pénzed a jegyre, kilépsz a kastélyból, és vége a játéknak')
                                                        print('\t 2 - Maradsz a kastélyban és beljebb mész')
                                                        print('----------------------------------------------------------------------------')
                                                        maradsz_e = 3
                                                        while maradsz_e > 2 or maradsz_e < 1:
                                                            maradsz_e = int(input('Választásod: '))
                                                        match maradsz_e:
                                                            case 1:
                                                                print('\n')
                                                                print('----------------------------------------------------------------------------')
                                                                prRed('\tKiléptél a kastélyból.')
                                                                prRed('\tA játéknak vége.')
                                                                print('----------------------------------------------------------------------------')
                                                                break
                                                            case 2:
                                                                orok_vagy_kedves_ember = random.randint(1,2)
                                                                match orok_vagy_kedves_ember:
                                                                    case 1:
                                                                        #őrök
                                                                        print('\n')
                                                                        print('----------------------------------------------------------------------------')
                                                                        prRed('Mivel úgy döntöttél, hogy maradsz a kastélyban és beljebb mész jegy nélkül, az őrök eltávolítottak a kastélyból')
                                                                        prRed('\t A játéknak vége.')
                                                                        print('----------------------------------------------------------------------------')
                                                                        break
                                                                    case 2:
                                                                        # kedves ember
                                                                        print('\n')
                                                                        print('----------------------------------------------------------------------------')
                                                                        prGreen('Úgy döntöttél, hogy beljebb mész a kastélyba jegy nélkül, azonban őrök kezdtek haladni feléd.')
                                                                        prGreen('Szerencsére egy másik ember észrevette az őröket, és kedvességből adott neked egy kastély jegyet. ')
                                                                        prGreen('\t Kijátszottad a játékot, az utadat szabadon folytathatod a kastélyban!')
                                                                        print('----------------------------------------------------------------------------')
                                                                        break
                                            case 2:
                                                prRed('Nem sikerült eljutnod a kastélyba, a játéknak vége.')
                                                break
                                    case 2:
                                        prRed('Játék vége')
                                        break
                            case 2:
                                stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                energia -= 1
                                print('--------------------------------------------------------------------------------------------------')
                                eventek2.szk0()
                                print('--------------------------------------------------------------------------------------------------')
                                arany += 15
                                stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                print('\n')
                                print('\t 1 - Igen')
                                prRed('\t 2 - Nem')
                                folytatas1 = 0
                                while folytatas1 > 2 or folytatas1 < 1:
                                    folytatas1 = int(input('Folytatod a játékot? '))
                                if folytatas1 == 1:
                                    print('\n')
                                    stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                    print('-------------------------------------------------------------------------------------')
                                    print('Opciók:')
                                    print('\t 1 - Belépsz a kastélyba ')
                                    prRed('\t 2 - Nem lépsz be a kastélyba')
                                    print('-------------------------------------------------------------------------------------')
                                    prPurple('Miután részt vettél a szerencsekerekezésben, megláttad a kastélyt és elindultál felé.')
                                    prPurple('Egy kisebb séta után elérkeztél a kastély bejáratához. ')
                                    print('-------------------------------------------------------------------------------------')
                                    belepsz_vagy_nem = 3
                                    while belepsz_vagy_nem > 2 or belepsz_vagy_nem < 1:
                                        belepsz_vagy_nem = int(input('Hogyan döntesz? '))
                                    energia -= 1
                                    match belepsz_vagy_nem:
                                        case 1:
                                            stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                            if kastelyjegy == 1:
                                                print('-------------------------------------------------------------------------------------')
                                                prPurple('Beléptél a kastélyba.')
                                                prPurple('Mivel volt egy korábbról szerzett jegyed, ezért a kastélyban jegyváráslás nélkül továbbmehetsz.')
                                                print('-------------------------------------------------------------------------------------')
                                                print('\n')
                                                prGreen('Sikeresen kijátszottad a játékot, az utadat szabadon folytathatod a kastélyban!') 
                                            else:
                                                print('\n')
                                                print('-------------------------------------------------------------------------------------')
                                                prPurple('Beléptél a kastélyba, viszont ahhoz hogy beljebb mehess venned kell egy jegyet!')
                                                print('')
                                                prPurple('\t1 jegy - 60 arany')
                                                print('-------------------------------------------------------------------------------------')
                                                print(f'Az aranyaid száma:{arany}')
                                                if arany >= 60:
                                                    print('------------------------')
                                                    print('Opciók')
                                                    print('\t 1 - Veszel jegyet')
                                                    print('\t 2 - Nem veszel jegyet')
                                                    print('------------------------')
                                                    veszeljegy = 3
                                                    while veszeljegy > 2 or veszeljegy < 1:
                                                        veszeljegy = int(input('Veszel jegyet? '))
                                                        match veszeljegy:
                                                            case 1:
                                                                arany -= 60
                                                                elszakad_vagy_nem = random.randint(1,2)
                                                                match elszakad_vagy_nem:
                                                                    case 1:
                                                                        eventek2.nemszakad()
                                                                        break
                                                                    case 2:
                                                                        eventek2.elszakad()
                                                                        break
                                                            case 2:
                                                                eventek2.nemvesz()
                                                                break
                                                else:
                                                    print('----------------------------------------------------------------------------')
                                                    print('Opciók')
                                                    prRed('\t 1 - Mivel nincs pénzed a jegyre, kilépsz a kastélyból, és vége a játéknak')
                                                    print('\t 2 - Maradsz a kastélyban és beljebb mész')
                                                    print('----------------------------------------------------------------------------')
                                                    maradsz_e = 3
                                                    while maradsz_e > 2 or maradsz_e < 1:
                                                        maradsz_e = int(input('Választásod: '))
                                                    match maradsz_e:
                                                        case 1:
                                                            eventek2.kileptel()
                                                            break
                                                        case 2:
                                                            orok_vagy_kedves_ember = random.randint(1,2)
                                                            match orok_vagy_kedves_ember:
                                                                case 1:
                                                                    #őrök
                                                                    eventek2.orok()
                                                                    break
                                                                case 2:
                                                                    # kedves ember
                                                                    eventek2.kedvesember()
                                                                    break
                                        case 2:
                                            prRed('Nem sikerült eljutnod a kastélyba, a játéknak vége.')
                                            break
                                else:
                                    prRed('Játék vége')
                                    break
                            case 3:
                                print('--------------------------------------------')
                                prLightPurple(f'Energia szinted:{energia}')
                                edessegeves = int(input('Mennyi édességet szeretnél enni, hogy növeld az energia szinted? (1 cukor -> +1 energia) '))
                                print('--------------------------------------------')
                                if edessegeves > cukor:
                                    print('\n')
                                    prLightPurple('Nincs elég cukrod. Meglátogatod az édesség boltot?')
                                    print('--------------------------------------------')
                                    print('\t1 - Igen')
                                    print('\t2 - Nem')
                                    print('--------------------------------------------')
                                    meglatogatod_e = 0
                                    while meglatogatod_e >2 or meglatogatod_e < 1:
                                        meglatogatod_e = int(input('Meglátogatod? '))
                                    match meglatogatod_e:
                                        case 1: 
                                            print('\n')
                                            print('--------------------------------------------')
                                            prLightPurple('Édesség bolt')
                                            print('')
                                            prLightPurple('1 cukor - 5 arany')
                                            print('\n')
                                            print('--------------------------------------------')
                                            prLightPurple(f'{arany} db aranyad van.')
                                            mennyit_veszel = int(input('Mennyi cukrot szeretnél venni? '))
                                            if arany >= mennyit_veszel*5:
                                                arany -= mennyit_veszel*5
                                                cukor += mennyit_veszel
                                                print('--------------------------------------------')
                                                prLightPurple(f'Vettél {mennyit_veszel} db cukrot. ')
                                                prLightPurple(f'Összes cukrod száma: {cukor}')
                                                print('--------------------------------------------')
                                                visszaugras3 = 1
                                            else: 
                                                print('--------------------------------------------')
                                                prLightPurple('Nincs elég aranyad')
                                                prLightPurple(f'Még {(mennyit_veszel*5) - arany } db aranyra van szükséged.')
                                                print('--------------------------------------------')
                                                visszaugras3 = 1
                                        case 2: 
                                            visszaugras3 = 1
                                elif edessegeves <= 0 or edessegeves > 10-energia:
                                    prLightPurple('Adj meg akkora mennyiséget, hogy ne legyen nagyobb az energiád 10-nél!')
                                    visszaugras3 = 1
                                elif edessegeves > 0 and edessegeves <= 10-energia:
                                    energia += edessegeves
                                    print('--------------------------------------------')
                                    prLightPurple(f'Az új energia szinted: {energia}')
                                    print('--------------------------------------------')
                                    visszaugras3 = 1
                            case 4:
                                print('\n')
                                print('--------------------------------------------')
                                prLightPurple('Édesség bolt')
                                print('')
                                prLightPurple('1 cukor - 5 arany')
                                print('\n')
                                print('--------------------------------------------')
                                prLightPurple(f'{arany} db aranyad van.')
                                mennyit_veszel = int(input('Mennyi cukrot szeretnél venni? '))
                                if arany >= mennyit_veszel*5:
                                    arany -= mennyit_veszel*5
                                    cukor += mennyit_veszel
                                    print('--------------------------------------------')
                                    prLightPurple(f'Vettél {mennyit_veszel} db cukrot. ')
                                    prLightPurple(f'Összes cukrod száma: {cukor}')
                                    print('--------------------------------------------')
                                    visszaugras3 = 1
                                else: 
                                    print('\n')
                                    prLightPurple('Nincs elég aranyad')
                                    prLightPurple(f'Még {(mennyit_veszel*5) - arany } db aranyra van szükséged.')
                                    visszaugras3 = 1
                            case 5:
                                print('\n')
                                prRed('Játék vége')
                                break
                case 2:
                    print('\n')
                    prRed('Játék vége') 
    else:
        prRed('Meghaltál, a játéknak vége. ')