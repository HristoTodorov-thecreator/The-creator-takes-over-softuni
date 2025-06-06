class Vehicle:
    def __init__(self,type,model,price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None


    def buy(self ,money: int, owner: str):
        if self.owner == None:
            if money >= self.price:
                self.owner = owner

                return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"
            else:
                return f'Sorry, not enough money'

        else:
            return f'Car already sold'






    def sell(self):
        if self.owner != None:
            self.owner = None
        else:
            return f'Vehicle has no owner'



    def __repr__(self):
        if self.owner != None:
            return f'{self.model} {self.type} is owned by: {self.owner}'
        else:
            return f'{self.model} {self.type} is on sale: {self.price}'



