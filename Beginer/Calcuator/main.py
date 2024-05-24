n =True
i = 0
while n:
    if i<1:
        x = int(input("Enter a number: "))
    op = input("Choose a operation (+,-,*,/): ")
    y = int(input("Enter a number: "))


    def calculate(x,y,op):
        global res 
        res = 0
        if op == '+': 
            res = x+y
        elif op == '-': 
            res = x-y 
        elif op == '*': 
            op = x*y 
        elif op == '/': 
            op = x/y
        return f"{x}{op}{y} = {res}" 
    
    if i <1:
        print(calculate(x,y,op))
    else: 
        print(calculate(res,y,op))

    i+=1
    ques = input("Put 'y' if you want to work with this result or put 'n' if you want to try new calculate: ")
    exit = input("Also you can write 'exit' and the program will end") 


    if ques == 'n': 
        i = 0 
        
    if exit == 'exit': 
        n = False
    
    
