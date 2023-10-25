import random
from statok import stat
def eventek():
    visszaugras = 1
    energia = stat(energia)
    eletero = stat(eletero)
    cukor = stat(cukor)
    arany = stat(arany)
#virágok
    eventcsoport1 = random.randint(2)
    match eventcsoport1:
        case 1 :
            #varázspóni
            print('Találkoztál egy varázspónival, ahogy a szökőkút felé mentél.')
            varazsponi = random.randint(2)
            match varazsponi:
                case 1: 
                    varazsponi = print('Összebarátkoztatok és elrepített varázsországba, és soha nem tértél vissza.')
                    print('Játék vége')
                    eletero = 0
                case 2:
                    varazsponi = print('Nem volt óvatos a varázs szarvával, ezért elvarázsolt egy időre. Kaptál még több energiát.')
        case 2:
            #erosszel
            print('Érkezett egy erős szél az utadon során.')
            erosszel = random.randint(2)
            match erosszel:
                case 1:
                    erosszel = print('Egy hónapig érvényes kastély-jegyet fújt az arcodba.')
                    kastelyjegy = 1
                case 2:
                    erosszel = print('Az erős szél miatt elestél, és lehorzsoltad a könyököd.')
                    eletero -= 3
    return eventcsoport1
                