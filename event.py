from map import player_y
from map import player_x

def event_eldont(player_x, player_y):
    match player_x:
        case 1:
            match player_y:
                case 1:
                    event = 25
                    #Stitch
                    return event
                case 2:
                    event = 10
                    #miklós patkány
                    return event
                case 3:
                    event = 3
                    #fotozas
                    return event
                case 4:
                    event = 11
                    #donald kacsa
                    return event
                case 5:
                    event = 13
                    #popcorn árus
                    return event
                case 6:
                    event = 16
                    # szél
                    return event
                case 7:
                    event = 19
                    #Dr. Simán prof.
                    return event
                case 8:
                    event = 20
                    #Barátnő
                    return event
                case 9:
                    event = 24
                    # Lajcsi király
                    return event
                case 10:
                    event = 28
                    #Jabba the hutt
                    return event
        case 2:
            match player_y:
                case 1:
                    event = -1
                    #spawn
                    return event
                case 2:
                    event = 2
                    #bohoc
                    return event
                case 3:
                    event = 4
                    #szökőkút
                    return event
                case 4:
                    event = 7
                    # pülss bolt
                    return event
                case 5:
                    event = 8
                    #szerencse jatek
                    return event
                case 6:
                    event = 9
                    #rudolf
                    return event
                case 7:
                    event = 17
                    #shrek
                    return event
                case 8:
                    event = 21 
                    #Boba a dagadt
                    return event
                case 9:
                    event = 27
                    #Darth VÖDÖR
                    return event
                case 10:
                    event = 30
                    #kastély
                    return event
        case 3:
            match player_y:
                case 1:
                    event = 1
                    #Magdi anyus jósnő
                    return event
                case 2:
                    event = 5
                    #ismerős
                    return event
                case 3:
                    event = 6
                    #gyerek
                    return event
                case 4:
                    event = 12
                    # JÉGKÁSA AUTOMATA
                    return event
                case 5:
                    event = 14
                    #varázs póni
                    return event
                case 6:
                    event = 15
                    #kalóz hajo
                    return event
                case 7:
                    event = 18
                    # Dr. Kocsis Ákos
                    return event
                case 8:
                    event = 22 
                    # Rosz csont jack
                    return event
                case 9:
                    event = 23
                    # Mici mackó
                    return event
                case 10:
                    event = 29
                    # Blaha Lujza tér
                    return event