from zoo.caretaker import Caretaker
from zoo.cheetah import Cheetah
from zoo.keeper import Keeper
from zoo.lion import Lion
from zoo.tiger import Tiger
from zoo.vet import Vet


class Zoo:
    def __init__(self,name,budget,animal_capacity,workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []


    def add_animal(self,animal, price):
        if price <= self.__budget and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price

            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
        elif price > self.__budget:
            return f'Not enough budget'
        else:
            return f'Not enough space for animal'



    def profit(self,amount):
        self.__budget += amount

    def hire_worker(self,worker):
        if len(self.workers) >= self.__workers_capacity:
            return f'Not enough space for worker'

        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self,worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total = sum(worker.salary for worker in self.workers)
        if self.__budget >= total:
            self.__budget -= total
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_care_cost = sum(animal.money_for_care for animal in self.animals)
        if self.__budget >= total_care_cost:
            self.__budget -= total_care_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def animals_status(self):
        lions = [a for a in self.animals if isinstance(a, Lion)]
        tigers = [a for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [a for a in self.animals if isinstance(a, Cheetah)]

        result = [f"You have {len(self.animals)} animals"]
        result.append(f"----- {len(lions)} Lions:\n" + "\n".join(str(l) for l in lions))
        result.append(f"----- {len(tigers)} Tigers:\n" + "\n".join(str(t) for t in tigers))
        result.append(f"----- {len(cheetahs)} Cheetahs:\n" + "\n".join(str(c) for c in cheetahs))

        return "\n".join(result)

    def workers_status(self):
        keepers = [w for w in self.workers if isinstance(w, Keeper)]
        caretakers = [w for w in self.workers if isinstance(w, Caretaker)]
        vets = [w for w in self.workers if isinstance(w, Vet)]

        result = [f"You have {len(self.workers)} workers"]
        result.append(f"----- {len(keepers)} Keepers:\n" + "\n".join(str(k) for k in keepers))
        result.append(f"----- {len(caretakers)} Caretakers:\n" + "\n".join(str(c) for c in caretakers))
        result.append(f"----- {len(vets)} Vets:\n" + "\n".join(str(v) for v in vets))

        return "\n".join(result)

