
def checking_ticket(currticket : str) -> str:
     if len(currticket) != 20:
         return 'invalid ticket'
     winning = ['@', '#', '$' ,'^' ]
     lpart = currticket[:10]
     rpart = currticket[10:]
     for currsymbol in winning:
         for check in range(10,5,-1):
             winning_symbol_rep = currsymbol * check
             if winning_symbol_rep in lpart and winning_symbol_rep in rpart:
                 if check == 10:
                     return f'ticket "{currticket}" - {check}{currsymbol} Jackpot!'
                 return f'ticket "{currticket}" - {check}{currsymbol}'

     return f'ticket "{currticket}" - no match'











tickets = [ticket.strip() for ticket in input().split(', ')]

for currticket in tickets:
    print(checking_ticket(currticket))

