# Vowel words
# Ivonne Mendoza
# ivonne@imendoza.io


# A more pythonic way for this: use a list to append, since split method 
# generates a list of words

def vowels(text:str)->str:
    # Since is only traverse every word I dont need to split the text
    # Individual characters
    new_string = []
    for char in text:
       # if the first character in the string is a vowel, return
        if char in 'aeiouAEIOU':
            new_string.append(char)
    return ''.join(new_string)


