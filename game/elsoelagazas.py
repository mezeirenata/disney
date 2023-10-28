import random
from statok import stat,eletero,player_ATK,player_DEF,energia,arany,cukor
import os
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk), end = '')

def menu1():
    eletero = 10
    player_ATK = 2
    player_DEF = 2
    energia = 10
    arany = 50
    cukor = 0
    egyenes = random.randint(1,3)
    jatekvege = 0
    if eletero > 0 and energia > 0:
        match egyenes:
            case 1:
                print('\n')
                print('----------------------------------------------------------------------------------------')
                prPurple('Egyenesen mentél volna tovább, azonban valaki megbotlott benned és elestetek mindketten.')
                prRed('\t-3 HP')
                print('----------------------------------------------------------------------------------------')
                eletero -= 3
            case 2:
                print('\n')
                print('---------------------------------------------------')
                prPurple('Tovább mentél egyenesen, azonban elakadtál egy nagy pocsolyánál.')
                prPurple('Mielőtt elgondolkozhattál volna, hogyan is kerüld ki, elvesztetted az egyensúlyod, és beleestél a pocsolyába.')
                prRed('\t-1 HP')
                print('---------------------------------------------------')
                eletero -= 1
            case 3:
                print('\n')
                print('----------------------------------------------------------------------------------------------------------------------')
                prPurple('Egyenesen mentél tovább, és mielőtt a szökőkúthoz értél volna megcsúszott a lábad és szerencsétlenül az arcodra estél.')
                prRed('\t-5 HP')
                print('----------------------------------------------------------------------------------------------------------------------')
                eletero -= 5
        visszaugras2 = 1
        prPurple('A történtek után elérkeztél a szökőkúthoz.')
        while visszaugras2 != 0 and eletero > 0:
            visszaugras2 = 0
            energia -= 1
            print('\n')
            print('Opciók:')
            print('\t1 - Balra mész, a szökőkút körül')
            print('\t2 - Jobbra mész, a szökőkút körül')
            print('\t3 - Egyél édességet (növeld meg az energiaszinted)')
            print ('\t4 - Édesség bolt meglátogatása')
            prRed ('\t5 - Kilépés')
            print('---------------------------------------------------')
            prPurple('Jelenleg a szökőkútnál tartózkodsz.')
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
                    prPurple(f'Találkozol egy bohóccal és {bohoc}.')
                    if bohoc == 'kedves volt veled':
                        prGreen('Kaptál 1 db cukrot.')
                        cukor += 1
                    else:
                        prRed('Vesztettél 1 HP-t .')
                        eletero -= 1
                    print('--------------------------------------------')
                    energia -= 1
                case 2:
                        mesehos = random.randint(1,3)
                        if mesehos == 1:
                            if eletero <= 9:
                                eletero += 1
                                mitkapsz = 1
                            elif eletero < 10 and eletero >9:
                                mitkapsz = 10-eletero
                                eletero = 10
                            elif eletero == 10:
                                mitkapsz = 0
                            print('\n')
                            prPurple('Találkoztál Donald kacsával, aki felajánlott neked egy közös képet, ez jó kedvre derített.')
                            print('\t-----')
                            prGreen(f'\t+{mitkapsz} HP')
                            print('\t-----')
                        elif mesehos == 2:
                            print('\n')
                            prPurple('Találkoztál Shrek-kel. Közölted vele hogy fotózkodni szeretnél vele, de ő csak öt aranyadért cserébe egyezett bele.')
                            print('\t-------------')
                            prRed(f'\t-5 arany')
                            print('\t-------------')
                            arany -= 5
                        elif mesehos == 3:
                            print('\n')
                            prPurple('Találkoztál Miki egérrel, akitől kértél egy közös képet, azonban ellopta az összes cukrod.')
                            print('\t-------------')
                            prRed(f'\t- {cukor} cukor')
                            print('\t-------------')
                            cukor = 0
                        energia -=1
                case 3:
                        print('--------------------------------------------')
                        prLightPurple(f'Energia szinted:{energia}')
                        edessegeves = int(input('Mennyi édességet szeretnél enni, hogy növeld az energia szinted? (1 cukor -> +1 energia)'))
                        print('--------------------------------------------')
                        if edessegeves > cukor:
                            print('\n')
                            prLightPurple('Nincs elég cukrod. Meglátogatod az édesség boltot?')
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
                                    else: 
                                        print('--------------------------------------------')
                                        prLightPurple('Nincs elég aranyad')
                                        prLightPurple(f'Még {(mennyit_veszel*5) - arany } db aranyra van szükséged.')
                                        print('--------------------------------------------')
                                case 2: 
                                    pass
                        elif edessegeves <= 0 or edessegeves > 10-energia:
                            prLightPurple('Adj meg akkora mennyiséget, hogy ne legyen nagyobb az energiád 10-nél!')
                        elif edessegeves > 0 and edessegeves <= 10-energia:
                            energia += edessegeves
                            print('--------------------------------------------')
                            prLightPurple(f'Az új energia szinted: {energia}')
                            print('--------------------------------------------')
                        visszaugras2 = 1
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
                    else: 
                        print('\n')
                        prLightPurple('Nincs elég aranyad')
                        prLightPurple(f'Még {(mennyit_veszel*5) - arany } db aranyra van szükséged.')
                    visszaugras2 = 1
                case 5:
                    print('\n')
                    prRed('Játék vége')
                    jatekvege = -1
                    break
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
                tovabbmesz = int(input('\tTovább mész?')) 
            match tovabbmesz:
                case 1:
                    print('\n')
                    print('----------------------------------')
                    prPurple('Egyenesen mentél tovább')
                    print('----------------------------------')
                    energia -= 1
                    visszaugras3 = 1
                    while visszaugras3 != 0:
                        visszaugras3 = 0
                        stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                        print('Opciók:')
                        print('\t1 - Beállsz játszani (legalább 15 arannyal kell rendelkezned)')
                        print('\t2 - Nem állsz be játszani(Tovább mész) ')
                        print('\t3 - Egyél édességet (növeld meg az energiaszinted)')
                        print ('\t4 - Édesség bolt meglátogatása')
                        prRed ('\t5 - Kilépés')
                        print('--------------------------------------------')
                        prPurple('Egy szerencsekerék van hozzád közel. ')
                        print('--------------------------------------------')
                        mitteszel = 0
                        while mitteszel >6 or mitteszel < 1:
                            mitteszel = int(input('Mit teszel?'))
                        match mitteszel:
                            case 1:
                                energia -= 1
                                if arany >= 15:
                                    szerencsekerek = random.randint(1,6)
                                    match szerencsekerek:
                                        case 1:
                                            if arany >= 15:
                                                arany -= 15
                                            else:
                                                arany = 0
                                            print('--------------------------------------------------------------------------------------------------')
                                            prPurple('Beálltál játszani a szerencsekeréken, azonban nem volt szerencséd és elvesztettél egy kevés pénzt.')
                                            print('\t-----------')
                                            prRed('\t -15 arany ')
                                            print('\t-----------')
                                            print('--------------------------------------------------------------------------------------------------')
                                            stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                        case 2:
                                            arany = 0
                                            print('-----------------------------------------------------------------------------')
                                            prPurple('Beálltál játszani és szerencsétlenséged okán elvesztetted az összes aranyad. ')
                                            prRed(f'-{arany} arany')
                                            print('-----------------------------------------------------------------------------')
                                            stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                        case 3:
                                            arany += 15
                                            print('-----------------------------------')
                                            prPurple('Beálltál szerencsekerekezni, és nyertél egy kevés aranyat')
                                            print('\t----------')
                                            prGreen('\t +15 arany ')
                                            print('\t----------')
                                            print('-----------------------------------')
                                            stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                        case 4:
                                            arany += 50
                                            print('-----------------------------------')
                                            prPurple('Beálltál játszani és rengeteg aranyat nyertél. Most nagyon szerencsés voltál.')
                                            print('\t----------')
                                            prGreen('\t "+50 arany ')
                                            print('\t----------')
                                            print('-----------------------------------')
                                            stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                        case 5:
                                            if arany >= 15:
                                                arany -= 15
                                            else:
                                                arany = 0
                                            print('--------------------------------------------------------------------------------------------------')
                                            prPurple('Beálltál játszani a szerencsekeréken, azonban nem volt szerencséd és elvesztettél egy kevés pénzt.')
                                            print('\t-----------')
                                            prRed('\t -15 arany ')
                                            print('\t-----------')
                                            print('--------------------------------------------------------------------------------------------------')
                                            stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                        case 6:
                                            print('-----------------------------------')
                                            prPurple('Hiába álltál be játszani, sajnos nem nyertél semmit.')
                                            prPurple('Tessék egy kastélyjegy, kiengesztelésből!')
                                            print('\t---------------')
                                            prGreen('\t + kastélyjegy ')
                                            print('\t---------------')
                                            print('-----------------------------------')
                                            kastelyjegy = 1
                                            stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                else:
                                    print('\n')
                                    prLightPurple('Nincs elég aranyad, hogy játssz')
                                    visszaugras3 = 1
                                print('\n')
                                print('---------------')
                                print('\t 1 - Igen')
                                print('\t 2 - Nem')
                                print('---------------')
                                folytatas1 = 0
                                while folytatas1 > 2 or folytatas1 < 1:
                                    folytatas1 = int(input('Folytatod a játékot?'))
                                while folytatas == 1:
                                    folytatas = 0
                                    stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                    print('\n')
                                    print('Opciók:')
                                    print('\t 1 - Belépsz a kastélyba ')
                                    prRed('\t 2 - Nem lépsz be a kastélyba')
                                    print('\t 3 - Egyél édességet (növeld meg az energiaszinted)')
                                    print ('\t 4 - Édesség bolt meglátogatása')
                                    print('-------------------------------------------------------------------------------------')
                                    prPurple('Miután részt vettél a szerencsekerekezésben, megláttad a kastélyt és elindultál felé.')
                                    prPurple('Egy kisebb séta után elérkeztél a kastély bejáratához. ')
                                    print('-------------------------------------------------------------------------------------')
                                    belepsz_vagy_nem = 5
                                    while belepsz_vagy_nem > 4 or belepsz_vagy_nem < 1:
                                        belepsz_vagy_nem = int(input('Hogyan döntesz?'))
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
                                                prLightPurple(f'Az aranyaid száma:{arany}')
                                                if arany >= 60:
                                                    print('------------------------')
                                                    print('Opciók')
                                                    print('\t 1 - Veszel jegyet')
                                                    print('\t 2 - Nem veszel jegyet')
                                                    print('------------------------')
                                                    veszeljegy = 3
                                                    while veszeljegy > 2 or veszeljegy < 1:
                                                        veszeljegy = int(input('Veszel jegyet?'))
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
                                        case 3:
                                            print('--------------------------------------------')
                                            prLightPurple(f'Energia szinted:{energia}')
                                            edessegeves = int(input('Mennyi édességet szeretnél enni, hogy növeld az energia szinted? (1 cukor -> +1 energia)'))
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
                                                    meglatogatod_e = int(input('Meglátogatod?'))
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
                                                            folytatas = 1
                                                        else: 
                                                            print('--------------------------------------------')
                                                            prLightPurple('Nincs elég aranyad')
                                                            prLightPurple(f'Még {(mennyit_veszel*5) - arany } db aranyra van szükséged.')
                                                            print('--------------------------------------------')
                                                            folytatas = 1
                                                    case 2: 
                                                        folytatas = 1
                                            elif edessegeves <= 0 or edessegeves > 10-energia:
                                                prLightPurple('Adj meg akkora mennyiséget, hogy ne legyen nagyobb az energiád 10-nél!')
                                                visszaugras3 = 1
                                            elif edessegeves > 0 and edessegeves <= 10-energia:
                                                energia += edessegeves
                                                print('--------------------------------------------')
                                                prLightPurple(f'Az új energia szinted: {energia}')
                                                print('--------------------------------------------')
                                                folytatas = 1
                                        case 4 :
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
                                                folytatas = 1
                                            else: 
                                                print('\n')
                                                prLightPurple('Nincs elég aranyad')
                                                prLightPurple(f'Még {(mennyit_veszel*5) - arany } db aranyra van szükséged.')
                                                folytatas = 1
                                else:
                                    prRed('Játék vége')
                                    break
                            case 2:
                                stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                energia -= 1
                                print('--------------------------------------------------------------------------------------------------')
                                prPurple('Mivel úgy döntöttél, hogy kihagyod a szerencsekerekezést, ezért elindultál tovább, azonban megláttál a földön valamit.')
                                prPurple('Jobban megnézted, és kiderült, hogy 15 arany volt a földön. Ez aztán a szerencse! ')
                                print('\t-----------')
                                prGreen('\t +15 arany ')
                                print('\t-----------')
                                print('--------------------------------------------------------------------------------------------------')
                                arany += 15
                                stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                print('\n')
                                print('\t 1 - Igen')
                                print('\t 2 - Nem')
                                folytatas1 = 0
                                while folytatas1 > 2 or folytatas1 < 1:
                                    folytatas1 = int(input('Folytatod a játékot?'))
                                if folytatas1 == 1:
                                    stat(eletero,player_ATK,player_DEF,energia,arany,cukor)
                                    print('\n')
                                    print('Opciók:')
                                    print('\t 1 - Belépsz a kastélyba ')
                                    prRed('\t 2 - Nem lépsz be a kastélyba')
                                    print('\t 3 - Egyél édességet (növeld meg az energiaszinted)')
                                    print ('\t 4 - Édesség bolt meglátogatása')
                                    print('-------------------------------------------------------------------------------------')
                                    prPurple('Miután részt vettél a szerencsekerekezésben, megláttad a kastélyt és elindultál felé.')
                                    prPurple('Egy kisebb séta után elérkeztél a kastély bejáratához. ')
                                    print('-------------------------------------------------------------------------------------')
                                    belepsz_vagy_nem = 5
                                    while belepsz_vagy_nem > 4 or belepsz_vagy_nem < 1:
                                        belepsz_vagy_nem = int(input('Hogyan döntesz?'))
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
                                                        veszeljegy = int(input('Veszel jegyet?'))
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
                                                                    prGreen('Úgy döntöttél, hogy beljebb mész a kastélyba jegy nélkül, azonban őrök kezdtek haladni feléd')
                                                                    prGreen('Szerencsére egy másik ember észrevette az őröket, és kedvességből adott neked egy kastély jegyet. ')
                                                                    prGreen('\t Kijátszottad a játékot, az utadat szabadon folytathatod a kastélyban!')
                                                                    print('----------------------------------------------------------------------------')
                                                                    break
                                        case 2:
                                            prRed('Nem sikerült eljutnod a kastélyba, a játéknak vége.')
                                            break
                                        case 3:
                                            print('--------------------------------------------')
                                            prLightPurple(f'Energia szinted:{energia}')
                                            edessegeves = int(input('Mennyi édességet szeretnél enni, hogy növeld az energia szinted? (1 cukor -> +1 energia)'))
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
                                                    meglatogatod_e = int(input('Meglátogatod?'))
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
                                        case 4 :
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
                                else:
                                    prRed('Játék vége')
                                    break
                            case 3:
                                print('--------------------------------------------')
                                prLightPurple(f'Energia szinted:{energia}')
                                edessegeves = int(input('Mennyi édességet szeretnél enni, hogy növeld az energia szinted? (1 cukor -> +1 energia)'))
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
                                        meglatogatod_e = int(input('Meglátogatod?'))
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
                    