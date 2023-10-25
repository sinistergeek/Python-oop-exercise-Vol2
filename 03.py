class Person:

    instances = []
    
    def __init__(self):
        Person.instances.append(self)

    @classmethod
    def count_instances(cls):
        return len(Person.instances)

p1 = Person()
p2 = Person()
P3 = Person()
print(Person.count_instances())
