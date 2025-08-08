import random
import time
from .constants import shop_items

def basic_atk(player):
    if random.randint(1, 100) <= player.cri_luk:
        damage = player.attack * 2
        print(f"치명타!!! 데미지:{damage}\n")
    else:
        damage = player.attack
        print(f"기본공격!! 데미지:{damage}\n")
        return damage

def skill_atk(player):
    print("\n[스킬]")
    for idx, skill in enumerate(player.skills):
        print(f"{idx + 1}. {skill["name"]} (MP소모:{skill["mp_cost"]}, 데미지 배수:{skill["damage_multiple"]})")
    while True:
        try:
            skill_choice = int(input("사용할 스킬을 선택해주세요:")) - 1
        except TypeError:
            print("잘못된 선택입니다. 스킬을 다시 선택해주세요")
            continue
        if 0 <= skill_choice < len(player.skills):
            skill = player.skills[skill_choice]
            if player.mp >= skill["mp_cost"]:
                player.mp -= skill["mp_cost"]
                damage = player.attack * skill["damage_multiple"]
                print(f"\n{player.nickname}가 {skill["name"]}을 시전하였습니다. {damage} 데미지\n")
                return damage
            else:
                print("MP가 부족합니다. 기본 공격을 수행합니다.")
                return basic_atk(player)
        else:
            print("잘못된 선택입니다. 기본 공격을 수행합니다")
            return basic_atk(player)






def player_turn(player):
    print("\n행동을 선택하세요")
    print("1. 기본 공격")
    print("2. 스킬 공격")
    action = input("선택 : ")

    if action == "1":
        return basic_atk(player)
        #기본 공격 함수 호출
    elif action == "2":
        return skill_atk(player)
#스킬 공격 함수 호출
    else:
        print("잘못된 입력입니다. 기본 공격을 수행합니다")
        return basic_atk(player)


#스킬공격 함수 호출




def battle(player, monster):
    print(f"{player.nickname} vs {monster.name}")
    while player.hp > 0 and monster.hp > 0:
        print("\n===================================================")
        print(f"{player.nickname} [HP: {player.hp}, MP: {player.mp}]")
        print(f"{monster.name} [HP: {monster.hp}]")

        #플레이어 턴
        damage = player_turn(player)
        monster.hp -= damage

        time.sleep(2)

        #플레이어가 이긴 경우
        if monster.hp <= 0:
            print(f"{monster.name}을/를 처치했습니다")
            #배틀보상
            exp_reward_multiple = random.uniform(0.9, 1.1)
            gold_reward_multiple = random.uniform(0.9, 1.1)
            exp_reward = int(monster.exp_reward * exp_reward_multiple)
            gold_reward = int(monster.gold_reward * gold_reward_multiple)
            print(f"\n결험치 - {exp_reward}, 골드 - {gold_reward} 획득!\n")
            player.gain_exp((exp_reward))
            player.gold += gold_reward
            #몬스터의 데이터와 플레이어의 데이터 초기화
            monster.hp = monster.max_hp
            player.hp =  player.max_hp
            player.mp = player.max_mp
            break

        #몬스터 턴
        player.hp -= monster.attack
        print(f"{monster.name}의 반격! {monster.attack} 데미지!")

        time.sleep(2)

        #플레이어가 몬스터에게 패배한 경우
        if player.hp <= 0:
            print("패배했습니다. 게임 오버!")
            #플레이어가 소지하고 있던 아이템을 초기화
            player.player_died()
            player.hp = player.max_hp
            player.mp = player.max_mp
            break

        #마나 회복 시스템
        player.mp_recovery(5)

#상점함수
def shop(player):
    print(f"\n보유 골드: {player.gold}")
    for idx, item in enumerate(shop_items):
        print(f"{idx +1}.{item["name"]} (추가 공격력: {item["attack"]}, 추가 hp: {item["hp"]}, 추가 mp: {item["mp"]} 추가 치명타 확률: {item["cri_luk"]}, 가격: {item["price"]})")
    while True:
        try:
            choice = int(input("구매할 아이템 번호를 입력해주세요(취소0): ")) - 1
        except ValueError:
            print("잘못된 입력입니다")
            continue
        if 0 <= choice < len(shop_items):
            item = shop_items[choice]
            if player.gold >= item["price"]:
                player.gold -= item["price"]
                player.items.append(item)  # 단순히 플레이어의 아이템 리스트에 추가
                player.apply_item(item)
                # 아이템 수치 적용
                print(f"{item["name"]}을/를 구매했습니다")
                print(f"남은 골드 : {player.gold}")
                break
            else:
                print("골드가 부족합니다")
                continue
        elif choice == -1:
            print("구매를 취소했습니다")
            break
        else:
            print("잘못된 입력입니다")
            continue



