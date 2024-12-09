st_dict = {}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_students = sorted(students)

i = 0
for j in list_students:
    st_dict[list_students[i]] = sum(grades[i]) / len(grades[i])
    i += 1

print(st_dict)
