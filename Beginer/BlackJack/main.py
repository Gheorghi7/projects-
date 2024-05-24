import random


bid = int(input("Enter yur bid(from 100 to 500 by 100): "))

card_digit =[2,3,4,5,6,7,8,9,10]
rand_digit = random.choice(card_digit)

card_suits = 10
ace = [1,11]
ace_rand = random.choice(ace)

score_p = 0
score_e = 0
game = True
while game:

#радомайзер карт 
    def rand_card(d,s,t):
        global card,enemy,cards
        card=[]
        enemy = []
        cards = [d,s,t]
        x_p = random.choice(cards)
        x_e = random.choice(cards)
        for i in range(2):
            if x_p == 11 or x_p == 1 : 
                card.append(int(input("Enter a  value 1 or 11: ")))
            else:
                card.append(x_p)
            if x_e == 11 or x_e == 1 : 
                card.append(x_e)
            else: 
                enemy.append(x_e)

#добавление еще одной карты в колоду
    def add_card(p=0,e=0):
        global cards
        x_p = random.choice(cards)
        x_e = random.choice(cards)
        if p == 1: 
            if x_p == 11 or x_p == 1 : 
                card.append(int(input("Enter a value 1 or 11")))
            card.append(x_p)
        if e == 1:
            if x_e == 11 or x_e == 1 : 
                card.append(random.choice(ace))
            enemy.append(random.choice(cards))


    rand_card(rand_digit,card_suits,ace_rand)
    
    print(card)
    
    ans = input('Add one more card?: ')
    if ans == 'yes': 
        p = 1 
    else: 
        p = 0
    
    if int(sum(enemy)) < 21: 
        e = 1 
    else: 
        e = 0
    
    add_card(p,e)
#счётчик очков
    score_e = sum(enemy)
    score_p = sum(card)

    if score_e == 21: 
        print(f"Enemy win!! {enemy} = {score_e}")   
        game = False
    elif score_p == 21: 
        print(f"You win!! {card} = {score_p}")        
        game = False
    elif score_p>21 and score_e>21: 
        print(f"Draw lose every person!! enemy = {enemy} , i = {card}")
    elif score_p > 21: 
        print(f"Your score more than 21!! {card}")
        print(f"Enemy win!!{enemy}") 
        game = False
    elif score_e > 21: 
        print(f"Enemy score more than 21!! {enemy}")
        print(f"You win!!{card}")
        game = False 
    elif score_p<21 and score_e<21: 
        if score_p == score_e: 
            print(f"Draw {card} == {enemy}")
            game = False
        elif score_p > score_e: 
            print(f"You win!! {card}>{enemy}")
            game = False 
        else: 
            print(f"Enemy win!! {enemy}>{card}")
            game = False
        

