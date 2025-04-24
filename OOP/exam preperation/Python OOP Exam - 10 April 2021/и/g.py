import unittest
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from controller import Controller


# Тест за Ornament
decoration = Ornament()
print(decoration.comfort)  # Очаквано: 1
print(decoration.price)    # Очаквано: 5

# Тест за Plant
plant = Plant()
print(plant.comfort)  # Очаквано: 5
print(plant.price)    # Очаквано: 10

# Тест за DecorationRepository
repo = DecorationRepository()
repo.add(decoration)
print(len(repo.decorations))  # Очаквано: 1
print(repo.remove(decoration))  # Очаквано: True
print(len(repo.decorations))  # Очаквано: 0
print(repo.find_by_type("Ornament"))  # Очаквано: "None"

# Тест за FreshwaterFish
fish = FreshwaterFish("Nemo", "Clownfish", 10)
print(fish.name)  # Очаквано: Nemo
print(fish.species)  # Очаквано: Clownfish
print(fish.size)  # Очаквано: 3
print(fish.price)  # Очаквано: 10
fish.eat()
print(fish.size)  # Очаквано: 6

# Тест за SaltwaterFish
fish2 = SaltwaterFish("Dory", "Blue Tang", 15)
print(fish2.name)  # Очаквано: Dory
print(fish2.species)  # Очаквано: Blue Tang
print(fish2.size)  # Очаквано: 5
print(fish2.price)  # Очаквано: 15
fish2.eat()
print(fish2.size)  # Очаквано: 7

# Тест за FreshwaterAquarium
aquarium = FreshwaterAquarium("Fresh Tank")
print(aquarium.name)  # Очаквано: Fresh Tank
print(aquarium.capacity)  # Очаквано: 50
print(len(aquarium.fish))  # Очаквано: 0

fish3 = FreshwaterFish("Goldie", "Goldfish", 20)
print(aquarium.add_fish(fish3))  # Очаквано: "Successfully added FreshwaterFish to Fresh Tank."
print(len(aquarium.fish))  # Очаквано: 1

aquarium.add_decoration(plant)
print(len(aquarium.decorations))  # Очаквано: 1
print(aquarium.calculate_comfort())  # Очаквано: 5

aquarium.feed()
print(aquarium.fish[0].size)  # Очаквано: 6 (пораснал с 3)

# Тест за Controller
controller = Controller()
print(controller.add_aquarium("FreshwaterAquarium", "Fresh Tank"))  # Очаквано: "Successfully added FreshwaterAquarium."
print(controller.add_decoration("Ornament"))  # Очаквано: "Successfully added Ornament."
print(controller.insert_decoration("Fresh Tank", "Ornament"))  # Очаквано: "Successfully added Ornament to Fresh Tank."

controller.add_fish("Fresh Tank", "FreshwaterFish", "Goldie", "Goldfish", 20)
print(controller.feed_fish("Fresh Tank"))  # Очаквано: "Fish fed: 1"
print(controller.calculate_value("Fresh Tank"))  # Очаквано: "The value of Aquarium Fresh Tank is 25.00."
