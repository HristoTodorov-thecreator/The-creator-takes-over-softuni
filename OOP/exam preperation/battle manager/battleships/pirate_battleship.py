from project.battleships.base_battleship import BaseBattleship

class PirateBattleship(BaseBattleship):
    INITIAL_AMMUNITION = 80
    def __init__(self,name: str, health: int, hit_strength: int):
        super().__init__(name,health,hit_strength,PirateBattleship.INITIAL_AMMUNITION)
    def attack(self):
        self.ammunition = max(self.ammunition - 10, 0)