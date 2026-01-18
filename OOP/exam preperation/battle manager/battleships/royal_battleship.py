from project.battleships.base_battleship import BaseBattleship

class RoyalBattleship(BaseBattleship):
    INITIAL_AMMUNITION = 100
    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name,health,hit_strength,RoyalBattleship.INITIAL_AMMUNITION)
    def attack(self):
        self.ammunition = max(self.ammunition - 25,0)