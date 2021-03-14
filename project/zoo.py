from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"
        elif self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        the_workers = [worker for worker in self.workers if worker.name == worker_name]
        if the_workers:
            current_worker = the_workers[0]
            self.workers.remove(current_worker)
            return f"{worker_name} fired successfully"
        else:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries_cost = 0
        for worker in self.workers:
            salaries_cost += worker.salary
        if self.__budget < salaries_cost:
            return f"You have no budget to pay your workers. They are unhappy"
        self.__budget -= salaries_cost
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        tend_cost = 0
        for animal in self.animals:
            tend_cost += animal.get_needs()
        if self.__budget < tend_cost:
            return f"You have no budget to tend the animals. They are unhappy."
        self.__budget -= tend_cost
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]
        res = f"You have {len(self.animals)} animals\n"
        res += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            res += repr(lion) + "\n"
        res += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            res += repr(tiger) + "\n"
        res += f"----- {len(cheetahs)} Cheetahs:\n"
        for c in cheetahs:
            res += repr(c) + "\n"
        res = res[:-1]
        return res

    def workers_status(self):
        caretakers = [a for a in self.workers if a.__class__.__name__ == "Caretaker"]
        keepers = [a for a in self.workers if a.__class__.__name__ == "Keeper"]
        vets = [a for a in self.workers if a.__class__.__name__ == "Vet"]
        res = f"You have {len(self.workers)} workers\n"
        res += f"----- {len(keepers)} Keepers:\n"
        for keep in keepers:
            res += repr(keep) + "\n"
        res += f"----- {len(caretakers)} Caretakers:\n"
        for carer in caretakers:
            res += repr(carer) + "\n"
        res += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            res += repr(vet) + "\n"
        res = res[:-1]
        return res