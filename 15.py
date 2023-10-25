class Vector:

    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

    def __str__(self):
        return f'{self.componenets}'

    def __len__(self):
        return len(self.componenets)

v1 = Vector(4,2)
v2 = Vector(-1, 3)

try:
    v1+v2
except TypeError as error:
    print(error)
