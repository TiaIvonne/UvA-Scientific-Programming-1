# Text Statistics
# Ivonne Mendoza
# ivonne@imendoza.io


def number_of_letters_in(text:str)->int:
    counter:int = 0
    temp = text.replace(" ", "").replace(".","")
    for char in temp:
        # print(char)
        # if the character is a number don't count in
        # if char not in "123456789":
        if char.isalpha():
            counter += 1
    return counter


def number_of_words_in(text:str)->int:
    counter:int = 0
    # str.split split every word
    for char in str.split(text):
        # print(char)
        counter += 1
    return counter

def number_of_sentences_in(text:str)->int:
    counter:int = 0
    temp:list = text.split(".")
    # this time split text by punctuation .
    for char in temp:
        # if char.strip() True by definition, so evaluates if there is a text
        # Whitespaces and empty are considerate empty so -> False
        if char.strip():
            counter += 1
    return counter

def average_word_length(text:str)->int:
    suma:int = 0
    counter:int = 0
    temp = text.replace(";","").replace(".","")
    text_splitted = temp.split()
    #print(text_splitted)
    for char in text_splitted:
        # Calculates total words in the sentence
        counter += 1
        #sums every word length
        suma += len(char)
    #print(counter)
    #print(suma)
    return suma/counter

