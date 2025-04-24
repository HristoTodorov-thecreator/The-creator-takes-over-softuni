from project.software.software import Software
from math import floor

class LightSoftware(Software):
    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        adjusted_capacity = floor(capacity_consumption * 1.5)
        adjusted_memory = floor(memory_consumption * 0.5)
        super().__init__(name, 'Light', adjusted_capacity, adjusted_memory)