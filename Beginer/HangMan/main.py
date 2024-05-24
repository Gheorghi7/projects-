import random
import time


words = ['mom','radio','dealer','soul','recognize','adopt']
rand_word = list(random.choice(words))
live = 5
Toggle = True
A = [0
     ]*len(rand_word)

isk = []

while live>0 and Toggle:
    
    print(A,' ', live)
    
    letter = input('Input letter: ')

    
    #проверяет на наличие буквы в слове
    if letter in rand_word: 
        print('Your letter is correct')
        
    #логика добавления буквы 
        for i in range(len(rand_word)):
            if i not in isk: 
                    if rand_word[i] == letter: 
                        A[i] = rand_word[i]           
                        isk.append(i)
                        break
                    
    #выводится когда все буквы найдены 
    if A == rand_word: 
        print(A)
        print("Congratulations, you win!!!")
        time.sleep(2)
        Toggle = False


    #Потеря жизни 
    elif letter not in rand_word: 
        live-=1
        print('Ops, wrong letter, try again')
        
    

    
    
    