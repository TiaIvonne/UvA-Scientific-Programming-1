# Alice
# Ivonne Mendoza
# ivonne@imendoza.io




#Contrary to earlier to the assignment you do need to strip all punctuation (,;:!?()-) and whitespacing (\t\n ) from the words.
# If i get rid of dash checkpy doesnt work

def longest_word_clean(text)->str:
    with open('./alice.txt', 'r') as f:
        # strip solo elimina al principio y final del string no a traves del texto
        my_file = f.read().replace(',', '').replace(';', '').replace(':', '')\
            .replace('!',' ').replace('?', ' ').replace('()', ' ')\
            .replace('\n', '').replace('\t', '')
        largest_word: str = ''
        for line in my_file.split(' '):
            if len(line) > len(largest_word):
                largest_word = line
        return largest_word
