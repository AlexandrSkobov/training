class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
       if new_floor < 1 or new_floor > self.number_of_floors:
           return 'Такого этажа не существует'
       else:
           return new_floor



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Одинград', 15)

print(h1.go_to(5))
print(h2.go_to(10))
print(h3.go_to(16))