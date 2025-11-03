# list_words
# Ivonne Mendoza
# ivonne@imendoza.io

def cleanup(word:str)->str:
    lower_text = word.lower().strip().replace(".","").replace(",","").replace("!","")
    clean = lower_text
    return clean

def text_to_unique_words(text):
    clean_text = cleanup(text)
    words = clean_text.split()
    new_words = []
    for word in words:
        if word not in new_words:
            new_words.append(word)

    return sorted(new_words)