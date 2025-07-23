def player_turn(player):
    print("행동을 선택하세요")
    print("1. 기본 공격")
    print("2. 스킬 공격")
    action = input("선택 : ")

    if action == "1":
        pass
        #기본 공격 함수 호출
    elif action == "2":
        pass
#스킬 공격 함수 호출
    else:
        pass

#스킬공격 함수 호출




def battle(player, monster):
    print(f"{player.nickname} vs {monster.name}")
    while player.hp > 0 and monster.hp > 0:
        print(f"{player.nickname} [HP: {player.hp}, MP: {player.mp}]")
        print(f"{monster.name} [HP: {monster.hp}]")

        #플레이어 턴


#=======================================================

