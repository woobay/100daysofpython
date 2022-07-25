import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
player = random.choices(cards, k=2)
computer = random.choices(cards,k=2)


def add_card(player):
    new_card = random.choice(cards)
    player.append(new_card)
    return sum(player)


def blackJack():
    win = True
    while win:
        if sum(player) == 21:
            print(f"You won! with {sum(player)} vs {sum(computer)}")
            break
        elif sum(computer) == 21:
            print(f"You loose! with {sum(player)} vs {sum(computer)}")
            win = False
            break
        elif sum(player) > 21: 
            if 11 in player:
                index = player.index(11)
                player[index] = 1
                
                if sum(player) > 21:
                    print(f"You loose! with {sum(player)} vs {sum(computer)}")

            else: 
                print(f"You loose! with {sum(player)} vs {sum(computer)}")
                break
        print(f"You cards are {player} with a total of {sum(player)}")
        if input("Do you want an other card? ") == "yes":
            add_card(player)
            
            
        elif sum(computer) < 17:
            while sum(computer) < 17:
                add_card(computer)
                if sum(computer) > 21:
                    win = False
                    print(f"You won! with {sum(player)} vs {sum(computer)}")
        else:
            if sum(player) > sum(computer):
                print(f"You won! with {sum(player)} vs {sum(computer)}")
                win = False

            else:
                print(f"You loose! with {sum(player)} vs {sum(computer)}")
                break


blackJack()

