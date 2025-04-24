from abc import ABC, abstractmethod


class BaseAstronaut(ABC):
    def __init__(self,id_number: str, salary: float, specialization: str, stamina: int):
        self.id_number = id_number
        self.salary  = salary
        self.specialization = specialization
        self.stamina = stamina

    @property
    def id_number(self):
        return self._id_number

    @id_number.setter
    def id_number(self, value):
        if not value.isdigit():
            raise ValueError("ID can contain only digits!")
        self._id_number = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0.0:
            raise ValueError("Salary must be a positive number!")
        self._salary = value

    @property
    def specialization(self):
        return self._specialization

    @specialization.setter
    def specialization(self, value):
        if not value.strip():
            raise ValueError("Specialization cannot be empty!")
        self._specialization = value

    @property
    def stamina(self):
        return self._stamina

    @stamina.setter
    def stamina(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Stamina is out of range!")
        self._stamina = value

    @abstractmethod
    def train(self):
        pass


