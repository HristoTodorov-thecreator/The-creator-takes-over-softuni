from animals.food import Meat
from animals.animals.animal import Bird
from animals.food import Vegetable
from animals.food import Fruit
from animals.food import Seed
class Owl(Bird):
    @staticmethod
    def make_sound():
        return 'Hoot Hoot'

    @property
    def allowed_food(self):
        return [Meat]

    @property
    def weight_increment(self):
        return 0.25



class Hen(Bird):
    @staticmethod
    def make_sound():
        return 'Cluck'

    @property
    def allowed_food(self):
        return [Vegetable,Fruit,Meat,Seed]

    @property
    def weight_increment(self):
        return 0.35
