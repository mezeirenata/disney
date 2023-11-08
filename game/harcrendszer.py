from random import randint
import os

enemy_HP = 50

def harc(player_ATK, player_DEF, player_DAM, player_HP, enemy_ATK, enemy_DEF, enemy_DAM, enemy_HP,):
    player_ATK = player_ATK
    player_DEF = player_DEF
    player_DAM = player_DAM
    player_HP = player_HP
    enemy_ATK = enemy_ATK
    enemy_DEF = enemy_DEF
    enemy_DAM = enemy_DAM
    enemy_HP = enemy_HP
    player_true_ATK = randint(1, 100) + player_ATK
    enemy_true_ATK = randint(1, 100) + enemy_ATK
    if player_true_ATK > enemy_DEF:
        win_player = "player"
    elif player_true_ATK == enemy_DEF:
        win_player = "draw"
    else:
        win_player = "enemy"
    if enemy_true_ATK > player_DEF:
        win_enemy = "enemy"
    elif enemy_true_ATK == player_DEF:
        win_enemy = "draw"
    else:
        win_enemy = "player"
    
    print("A te köröd következik")

    if win_player == "player":
        print("Talált a támadásod")
        enemy_HP -= player_DAM*randint(1, 4)
        if enemy_HP > 1:
            print(f"Ellenfeled életereje: {enemy_HP}")
        else:
            print("Ellenség meghalt")
            return
    elif win_player == "draw":
        print("Ez a köröd döntetlen.")
        print(f"Ellenfeled életereje: {enemy_HP}")
    elif win_player == "enemy":
        print("Az ellenfeled betalált")
        player_HP -= enemy_DAM*randint(1,4)
        if player_HP > 1:
            print(f"Az életerőd: {player_HP}")
        else:
            print("Meghaltál")
            return "halal"
    
    print("")
    print("Az ellenfeled köre következik")

    if win_enemy == "player":
        print("Talált a támadásod")

        enemy_HP -= player_DAM*randint(1, 4)
        if enemy_HP > 1:
            print(f"Ellenfeled életereje: {enemy_HP}")
        else:
            print("Ellenség meghalt")
            return "nyert"
    elif win_enemy == "draw":
        print("Ez a kör döntetlen.")
        print(f"Ellenfeled életereje: {enemy_HP}")
    elif win_enemy == "enemy":
        print("Az ellenfeled betalált")
        player_HP -= enemy_DAM*randint(1,4)
        if player_HP > 1:
            print(f"Az életerőd: {player_HP}")
        else:
            print("Meghaltál")
            return "halal"

    print("")
    harc_menu(player_ATK, player_DEF, player_DAM, player_HP, enemy_ATK, enemy_DEF, enemy_DAM, enemy_HP,)

def harc_menu(player_ATK, player_DEF, player_DAM, player_HP, enemy_ATK, enemy_DEF, enemy_DAM, enemy_HP,):

    if player_HP < 1:
        end =  "halal"
        return end
    elif enemy_HP < 1:
        end = "nyert"
        return end
    else:
        print("1 - Neki támadsz")
        print("2 - Elmenekülsz")
        valasz = int(input("Választásod: "))
        if valasz == 1:
            os.system("cls")
            end = harc(player_ATK, player_DEF, player_DAM, player_HP, enemy_ATK, enemy_DEF, enemy_DAM, enemy_HP,)
        else:
            end = "elfut"
            return end
        return end
end = harc_menu(40, 100, 4, 100, 30, 99, 2, enemy_HP,)