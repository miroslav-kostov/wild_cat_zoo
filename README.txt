In this exercise we are going to create a whole project called "Wild Cat Zoo". We are going to create the project step-by-step starting with the project structure:
 
Please create separate file for each class as shown above and submit a zip file containing all files (zip the whole project folder/module) - it is important to include all files in project module in order to be able to make proper imports.
Class Lion
Attributes
Public attribute name: string
Public attribute gender: string
Public attribute age: number
Methods
__init__(name, gender, age) - set all the attributes to the given ones
get_needs() - returns the number 50 (amount of money needed to tend the animal)
__repr__() - returns string representation of the lion in the format: "Name: {name}, Age: {age}, Gender: {gender}"
Class Tiger
Attributes
Public attribute name: string
Public attribute gender: string
Public attribute age: number
Methods
__init__(name, gender, age) - set all the attributes to the given ones
get_needs() - returns the number 45 (amount of money needed to tend the animal)
__repr__() - returns string representation of the tiger in the format: "Name: {name}, Age: {age}, Gender: {gender}"
Class Cheetah
Attributes
Public attribute name: string
Public attribute gender: string
Public attribute age: number
Methods
__init__(name, gender, age) - set all the attributes to the given ones
get_needs() - returns the number 60 (amount of money needed to tend the animal)
__repr__() - returns string representation of the cheetah in the format: "Name: {name}, Age: {age}, Gender: {gender}"
Class Keeper
Attributes
Public attribute name: string
Public attribute age: number
Public attribute salary: number
Methods
__init__(name, age, salary) - set all the attributes to the given ones
__repr__() - returns string representation of the keeper in the format: "Name: {name}, Age: {age}, Salary: {salary}"
Class Caretaker
Attributes
Public attribute name: string
Public attribute age: number
Public attribute salary: number
Methods
__init__(name, age, salary) - set all the attributes to the given ones
__repr__() - returns string representation of the caretaker in the format: "Name: {name}, Age: {age}, Salary: {salary}"
Class Vet
Attributes
Public attribute name: string
Public attribute age: number
Public attribute salary: number
Methods
__init__(name, age, salary) - set all the attributes to the given ones
__repr__() - returns string representation of the vet in the format: "Name: {name}, Age: {age}, Salary: {salary}"
Class Zoo
Attributes
Private attribute animal_capacity: number
Private attribute workers_capacity: number
Private attribute budget: number
Public attribute name: string
Public attribute animals: list (empty upon initialization)
Public attribute workers: list (empty upon initialization)
Methods
__init__(name, budget, animlal_capacity, workers_capacity) - set the attributes to the given ones
add_animal(animal, price)
-	If you have enough budget and capacity add the animal (instance of Lion/Tiger/Cheetah) to the animals list, reduce the budget and return "{name} the {type of animal (Lion/Tiger/Cheetah)} added to the zoo"
-	If you have capacity, but no budget, return "Not enough budget"
-	In any other case, you don't have space and you should return "Not enough space for animal"
hire_worker(worker)
-	If you have enough space for the worker (instance of Keeper/Caretaker/Vet), add him to the workers and return "{name} the {type(Keeper/Vet/Caretaker)} hired successfully"
-	Otherwise return "Not enough space for worker"
fire_worker(worker_name)
-	If there is a worker with that name in the workers list, remove him and return "{worker_name} fired successfully"
-	Otherwise return "There is no {worker_name} in the zoo"
pay_workers()
-	If you have enough budget to pay the workers (sum their salaries) pay them and return "You payed your workers. They are happy. Budget left: {left_budget}"
-	Otherwise return "You have no budget to pay your workers. They are unhappy"
tend_animals()
-	If you have enough budget to tend the animals reduce the budget and return "You tended all the animals. They are happy. Budget left: {left_budget}"
-	Otherwise return "You have no budget to tend the animals. They are unhappy."
profit(amount)
-	Increase the budget with the given amount of profit
animals_status()
-	Returns the following string:
You have {total_animals_count} animals
----- {amount_of_lions} Lions:
{lion1}
�
----- {amount_of_tigers} Tigers:
{tiger1}
�
----- {amount_of_cheetahs} Cheetahs:
{cheetah1}
�
-	Hint: use the __repr__ methods of the animals to print them on the console
workers_status()
-	Returns the following string:
You have {total_workers_count} workers
----- {amount_of_keepers} Keepers:
{keeper1}
�
----- {amount_of_caretakers} Caretakers:
{caretaker1}
�
----- {amount_of_vetes} Vets:
{vet1}
�
-	Hint: use the __repr__ methods of the workers to print them on the console
