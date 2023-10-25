class Vector:
    def __init__(self, *args):
        self.components = args

    def __repr(self):
        return f"VectorP{self.components}"

    def __str__(self):
        return f'{self.components}'

    def __len__(self):
        return len(self.components)

    def __add__(self, other):
        components = tuple(x + y for x,y in zip(self.components, other.components))
        return Vector(*components)


v1 = Vector(3,2)
v2 = Vector(5,2)
try:
    v1 - v2
except TypeError as error:
    print(error)
