word_dictionary= input("Ingresa palabras para crear el diccionario con este formato <palabra>:<traducción> y separado comas: \n->")

list_words_dictionary = word_dictionary.split(",")

print(list_words_dictionary)
dictionary = {}
for pair in list_words_dictionary:
    second_list_words = pair.split(":")
    dictionary[second_list_words[0]] = second_list_words[1]

print(dictionary)

words_to_translate = input("Ingresa una frase para traducir\n->")

list_words_to_translate = words_to_translate.split(" ")

print(list_words_to_translate)

for word in list_words_to_translate:
    print(dictionary.get(word,word), end=" ")