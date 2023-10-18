from event import event_eldont
from map import player_x
from map import player_y
import random

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
        case 3:
            print("Egy térre érkezel és 3 figura áll elötted. Gofy, Füles, Hamupipőke.")
            print("Válassz kivel fótózkodol.")
            print("1 - Goofy")
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