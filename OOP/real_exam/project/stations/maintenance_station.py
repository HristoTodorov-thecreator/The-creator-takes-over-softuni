from project.stations.base_station import BaseStation

class MaintenanceStation(BaseStation):
    def __init__(self, name: str):
        super().__init__(name, 3)

    def update_salaries(self, min_value: float):
        for astronaut in self.astronauts:
            if astronaut.specialization == "EngineerAstronaut" and astronaut.salary <= min_value:
                astronaut.salary += 3000.0