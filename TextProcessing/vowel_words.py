# Vowel words
# Ivonne Mendoza
# ivonne@imendoza.io


# A more pythonic way for this: use a list to append, since split method 
# generates a list of words

def vowel_words(text:str)->str:
    # Split the text by spaces
    temp = text.split(' ')
    new_string = ''
    for char in temp:
       # if the first character in the string is a vowel, return
        if char[:1] in 'aeiouAEIOU':
            new_string += char + ' '

    return new_string


