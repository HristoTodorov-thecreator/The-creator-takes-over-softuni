from animals.animals.animal import Mammal
from animals.food import Meat
from animals.animals.animal import Bird
from animals.food import Vegetable
from animals.food import Fruit
from animals.food import Seed
class Mouse(Mammal):
    @staticmethod
    def make_sound():
        return 'Squeak'

    @property
    def allowed_food(self):
        return [Vegetable, Fruit]

    @property
    def weight_increment(self):
        return 0.10



class Dog(Mammal):
    @staticmethod
    def make_sound():
        return 'Woof!'

    @property
    def allowed_food(self):
        return [Meat]

    @property
    def weight_increment(self):
        return 0.4


class Cat(Mammal):
    @staticmethod
    def make_sound():
        return 'Meow'

    @property
    def allowed_food(self):
        return [Meat,Vegetable]

    @property
    def weight_increment(self):
        return 0.30


class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return 'ROAR!!!'

    @property
    def allowed_food(self):
        return [Meat]

    @property
    def weight_increment(self):
        return 1.00
