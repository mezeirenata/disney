from map import player_y
from map import player_x

def event_eldont(player_x, player_y):
    match player_x:
        case 1:
            match player_y:
                case 1:
                    event = 0
                    #semmi
                case 2:
                    event = 10
                    #miklós patkány
                case 3:
                    event = 3
                    #fotozas
                case 4:
                    event = 11
                    #donald kacsa
                case 5:
                    event = 13
                    #popcorn árus
                case 6:
                    event = 16
                    # szél
                case 7:
                    event = 19
                    #DR Simán prof.
                case 8:

                case 9:

                case 10:
                    event = 28
                    #Jabba the hutt
        case 2:
            match player_y:
                case 1:
                    event = 0
                    #semmi
                case 2:
                    event = 2
                    #bohoc
                case 3:
                    event = 4
                    #szökőkút
                case 4:
                    event = 7
                    # pülss bolt
                case 5:
                    event = 8
                    #szerencse jatek
                case 6:
                    event = 9
                    #rudolf
                case 7:
                    event = 17
                    #shrek
                case 8:

                case 9:

                case 10:
                    event = 30
                    #kastély
        case 3:
            match player_y:
                case 1:
                    event = 1
                    #Magdi anyus jósnő
                case 2:
                    event = 5
                    #ismerős
                case 3:
                    event = 6
                    #gyerek
                case 4:
                    event = 12
                    # buff bolt
                case 5:
                    event = 14
                    #varázs póni
                case 6:
                    event = 15
                    #kalóz hajo
                case 7:
                    event = 18
                    # DR Kocsis Ákos
                case 8:

                case 9:

                case 10:
                    event = 29
                    # Blaha Lujza tér