print('\n# dict')
my_dict = { 'Alex':43,
            'Elena':40,
            'Masha':12,
            'Lena':55}
print(my_dict)
print(my_dict['Alex'])
print(my_dict.get('Lana'))
my_dict.update({'Svetlana':41,
                'Misha':29})
a = my_dict.pop('Lena')
print(a)
print(my_dict)

print('\n# set')
my_set = { 1,2,4,5,8,2,2,1,'apple',3,5,88.8,10,10,11,'apple'}
print(my_set)
e = 15,16
my_set.add(e)
print(my_set)
my_set.discard('apple')
print(my_set)