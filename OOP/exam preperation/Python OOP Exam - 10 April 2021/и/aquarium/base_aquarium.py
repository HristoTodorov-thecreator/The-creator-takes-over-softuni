from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self,name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: list = []
        self.fish = []
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        total = 0
        for i in self.decorations:
            total += i.comfort

        return total

    def add_fish(self,fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."

        fish_type = fish.__class__.__name__

        if fish_type not in ('SaltwaterFish',"FreshwaterFish" ):
            return

        self.fish.append(fish)

        return f"Successfully added {fish_type} to {self.name}."

    def remove_fish(self,fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self,decoration):
        self.decorations.append(decoration)

    def feed(self):
        [f.eat() for f in self.fish]

    def __str__(self):

        output = [f'{self.name}:', "Fish: "]
        if self.fish:
            output[1] += " ".join(f.name for f in self.fish)
        else:
            output[1] += 'none'

        output.append(f'Decorations: {len(self.decorations)}\n'
                      f'Comfort: {self.calculate_comfort()}')

        return '\n'.join(output)



