from movie.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    PRICE = 3.50
    MILLILITERS = 50


    def __init__(self,name,caffeine):
        super().__init__(name,Coffee.PRICE,Coffee.MILLILITERS)
        self.__caffeine = caffeine


    @property
    def caffeine(self):
        return self.__caffeine

