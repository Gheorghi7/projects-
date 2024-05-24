#Распечатывать имеющийся запас воды, молока,кофе. А так же распечатывать общее колличество денег в аппарате 
#Логика проверка наличия всех компонентов для приготовления кофе 3 видов, которые требуют разное количество ресурсов 
#Логика проверки 4 видов монет в 1,5,10,25 центов 
#Экспрессо : 50мл воды , 18гр кофе , цена 1.50
#Латэ : 200мл воды , 24гр коффе , 150мл молока , цена 2.50 
#Капучино : 250мл воды , 24гр коффе , 100мл молока, цена 3.00 
game = True 

while game:


    def expresso_fn(expresso):
        global report
        report = [500,80,280]
        report[0] = report[0]-expresso[1]
        report[1] = report[1] - expresso[2]
        return "Your expresso is ready!!♥"
        
    def latte_fn(latte): 
        report[0] = report[0]-latte[1]
        report[1] = report[1] - latte[2]
        report[2] = report[2]-latte[3]
        return "Your latte is ready!!♥"
    
    def cappuccino_fn(cappuccino): 
        report[0] = report[0]-cappuccino[1]
        report[1] = report[1] - cappuccino[2]
        report[2] = report[2]-cappuccino[3]
        return "Your cappuccino is ready!!♥"
    

    def money_fn(fn,coffe):
        global money 
        money = 0
        penny = 0.01 * int(input("How much penny: "))
        nickel = 0.05 * int(input("How much nickel: "))
        dime = 0.10 * int(input("How much dime: "))
        quarter = 0.25 * int(input("How much quarter: "))
        total_money = penny+nickel+dime+quarter
        if total_money>coffe[0]:
            change = total_money-coffe[0]
            print(f"Total we have {total_money}")
            total_money = total_money-change
            money+=total_money
            return fn(coffe),f"and your change {change}"
        money+=total_money
        return fn(coffe)
        
    


#drincs
    expresso = [1.50, 50, 12]
    latte = [2.50, 200, 24, 150]
    cappuccino = [3.00, 250, 24, 100]

    
    
    drink = input("What drink do you want?(expresso,latte,cappuccino): ")
    if drink == 'report': 
        res = f"water = {report[0]},\ncoffee = {report[1]},\nmilk = {report[2]},\nmoney = {money}"
        print(res)
    if drink == 'expresso':    
        print(money_fn(expresso_fn,expresso))
        
    elif drink == 'latte':
        print(money_fn(latte_fn,latte))
        
    elif drink == 'cappuccino':
        print(money_fn(cappuccino_fn,cappuccino))
        
    if report[0]<0 or report[1]<0 or report[2]<0: 
        print('Sorry the machin is empty, come back later pls')
        print(res)
        game = False
        
