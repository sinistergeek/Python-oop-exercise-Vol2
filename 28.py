class Vechicle:
    def __init__(self, category=None):
        self.category = category if category else 'land vechicle'

    def __repr__(self):
        return f"{self.__class__.__name__}(category='{self.category}')"

class LandVechicle(Vechicle):
    pass

class AirVechicle(Vechicle):
    def __init__(self, category=None):
        self.category = category if category else 'air vehicle'

instances = [Vechicle(), LandVechicle(), AirVechicle()]
for instance in instances:
    print(instance)
