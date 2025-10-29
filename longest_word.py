# Longest Word
# Ivonne Mendoza
# ivonne@imendoza.io

def longest_word(text:str)->str:
    largest_word: str = ''
    text_splitted = text.split()
    for char in text_splitted:
        # Compares and stores as a len_words
        if len(char) > len(largest_word):
            largest_word = char
    return largest_word

