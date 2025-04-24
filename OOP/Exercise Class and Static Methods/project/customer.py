from animals.idmixin import IDmixin

class Customer(IDmixin):



    def __init__(self,name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()
        self.increment_id()



    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"