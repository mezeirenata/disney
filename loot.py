from harcrendszer import enemy_HP

def loot_arany(arany):
    arany += round(enemy_HP/10)
    return arany

def loot_ATK(player_ATK):
    player_ATK += round(enemy_HP/15)
    return player_ATK

def loot_DEF(player_DEF):
    player_DEF += round(enemy_HP/17)
    return player_DEF