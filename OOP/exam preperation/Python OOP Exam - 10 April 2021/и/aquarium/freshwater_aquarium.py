from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    def __init__(self,name):
        super().__init__(name,self.initial_capacity)
        
    @property
    def initial_capacity(self):
        return 50