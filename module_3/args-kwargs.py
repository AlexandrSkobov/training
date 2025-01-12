import re

def single_root_words(root_word, *other_words):
    root_word = root_word.lower()
    r = re.compile(root_word)
    same_words = []
    oth_origin = other_words
    oth = []
    for i in other_words:
        oth.append(i.lower())

    for i in oth:
        if r.search(i):
            same_words.append(i)

    for j in oth:
        r2 = re.compile(j)
        if r2.search(root_word) and str.istitle(oth_origin[0]):
            same_words.append(j.title())

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)


