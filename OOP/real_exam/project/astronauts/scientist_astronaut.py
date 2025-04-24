from project.astronauts.base_astronaut import BaseAstronaut


class ScientistAstronaut(BaseAstronaut):
    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, "ScientistAstronaut", 70)

    def train(self):
        self.stamina = min(100, self.stamina + 3)