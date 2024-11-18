from traceback import print_tb

immutable_var = (8, True, 'stroka', [3,4])
print(immutable_var)
print(id(immutable_var[3][0]))
print(id(immutable_var[3]))
immutable_var[3][0] = 2
print(immutable_var)
print(id(immutable_var[3]))
print(id(immutable_var[3][0]))
# кортежи не изменяемый тип данных, однако, в этом примере, ссылки в списке изменить нельзя, а объект ссыки - можно менять

mutable_list = [ 'table', 'chair', 'sofa']
print(mutable_list)
mutable_list[0] = 'window'
mutable_list.append('door')
print(mutable_list)
