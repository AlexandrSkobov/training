class Human:
    head = True

    def __init__(self, name, age):
        self.name = name
        self.age = age


den = Human('den', 34)
max = Human('max', 34)
den.head = False

print(Human.__dict__)
print(den.__dict__)
print(max.head)
print(den.head)