from project.stations.base_station import BaseStation


class ResearchStation(BaseStation):
    def __init__(self, name: str):
        super().__init__(name, 5)

    def update_salaries(self, min_value: float):
        for astronaut in self.astronauts:
            if astronaut.specialization == "ScientistAstronaut" and astronaut.salary <= min_value:
                astronaut.salary += 5000.0