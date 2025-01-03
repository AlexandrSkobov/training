class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
       if new_floor < 1 or new_floor > self.number_of_floors:
           return 'Такого этажа не существует'
       else:
           return new_floor

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('ЖК Горский', 10)
h2 = House('Домик в деревне', 20)
h3 = House('ЖК Одинград', 15)

print(h1)
print(h2)
print(len(h1))
print(len(h2))