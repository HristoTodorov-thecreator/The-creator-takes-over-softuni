from abc import ABC, abstractmethod


class BaseStation(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.astronauts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not all(c.isalnum() or c == '-' for c in value):
            raise ValueError("Station names can contain only letters, numbers, and hyphens!")
        self._name = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("A station cannot have a negative capacity!")
        self._capacity = value

    def calculate_total_salaries(self):
        return f"{sum(a.salary for a in self.astronauts):.2f}"

    def status(self):
        astronaut_ids = "N/A" if not self.astronauts else " #".join(sorted(a.id_number for a in self.astronauts))
        return f"Station name: {self.name}; Astronauts: {astronaut_ids}; Total salaries: {self.calculate_total_salaries()}"

    @abstractmethod
    def update_salaries(self, min_value: float):
        pass
