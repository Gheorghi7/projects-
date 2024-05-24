auction_cust= {}
game = True 

while game:
    name = input("Enter your name:")
    bid = int(input("Enter the bid $: ")) 
    auction_cust[name] = bid
    x = input("yes or no: ")
    

    def find_h_b(auction_cust):
        high = 0
        winner = ''
        for i in auction_cust: 
            amount = auction_cust[i]
            if amount>high: 
                high = amount
                winner = i 
        print(f"The winner is {winner} with a bid of {high}")            
    

    if x == 'no':
        find_h_b(auction_cust)
        game = False 
        
    
            
        
        
    