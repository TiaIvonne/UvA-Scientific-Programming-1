# Snake case
# Ivonne Mendoza
# ivonne@imendoza.io



def snake_case(text:str)->str:
    words = []
    # For every char in the text checks
    # if finds a upper add a "_"
    # if not just append the character
    # This creates a list of separate characters like this
    # ['t', 'e', 'x', 't', '_P', 'r', 'o', 'c', 'e', 's', 's', 'i', 'n', 'g', '_V', 'a', 'r', 'i', 'a', 'b', 'l', 'e']

    for character in text:
        if character.isupper():
            words.append( "_"+ character)
        else:
            words.append(character)
    # so we need to join together and convert to lowercase
    new_string =  "".join(words)
    result = new_string.lower()
    return result







