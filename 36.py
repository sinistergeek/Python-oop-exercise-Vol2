class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.first_name = last_name
        self.age = age

class Department:
    pass

class Worker(Person, Department):
    pass

worker = Worker('John', 'Doe', 35)
print(worker.__dict__)
