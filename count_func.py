calls = 0

def count_calls(*args, **kwargs):               # unpack/
        global calls
        calls += 1
        return calls


def string_info(string):
    up_str = string
    l = len(up_str)
    upp = (up_str.upper())
    low = (up_str.lower())
    count_calls()
    return l, upp, low


def is_contains(string, list_to_search):
    string1 = string
    list1 = list_to_search
    result = False
    count_calls()
    for i in list1:
        if string1.lower() == i.lower():
            result = True
    return result


print(string_info('Capibara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('Group', ['grouD', 'groUP', 'Up']))
print(is_contains('Group', ['gro', 'groUP', 'Up']))
print(calls)