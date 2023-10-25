class StringListOnly(list):
    def append(self, string):
        if not isinstance(string, str):
            raise TypeError('Only objects of type str can be added to list.')
        super().append(string)

slo = StringListOnly()
slo.append('Data')
slo.append('Science')
print(slo)
