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

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, other):
        return self.number_of_floors + other

    def __radd__(self, other):
        return self.__add__

    def __iadd__(self, other):
        return self.__add__

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(h1 == h2)
h1.number_of_floors = h1.number_of_floors + 10
print(h1)
print(h1 == h2)
h1.number_of_floors += 10
print(h1)
h2.number_of_floors = 10 + h2.number_of_floors
print(h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)