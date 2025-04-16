def num_words(text):
    words = text.split()
    number_of_words = 0
    for word in words:
        number_of_words += 1
    return number_of_words

def count_characters(text):
    characters = {}
    charr = list(text.lower())
    for c in charr:
        if c not in characters:
            characters[c] = 1
        else:
            characters[c] += 1   
    return characters

def sorted_dictionaries(dickt):
    dictionaries_list = []
    for c in dickt:
        dictionaries_list.append({"character": c, "count": dickt[c]})
    sorted_list =  sorted(dictionaries_list, key=lambda x: x["count"], reverse=True)
    return sorted_list