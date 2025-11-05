# name: Ivonne Mendoza email: ivonne@imendoza.io
# This program calculates a score (positive, negative, neutral) based on a list of words


def cleanup(word:str)->str:
    """
    This function cleans a string (get rid of punctuation, spaces, etc.)
    """
    lower_text = word.lower().strip().replace(".","").replace(",","").replace("!","")
    clean = lower_text
    return clean

def load_words(filename)->list:
    """
    This function loads words from a text file
    """
    content = open(filename)
    lines = content.read().splitlines()
    content.close()
    return lines

def load_positive_words()->list:
    """
    This function returns a list of positive words from a text file
    """
    return load_words("./pos_words.txt")

def load_negative_words()->list:
    """
    This function returns a list of negative words from a text file
    """
    return load_words("./neg_words.txt")

def sentiment_of_word(word:str)->int:
    """
    sentiment_of_word returns a score based on positive or negative words
    if word doesn't exist on positive or negative it's considered neutral
    """
    positive = load_positive_words()
    negative = load_negative_words()
    # calls cleanup function
    clean = cleanup(word)
    total_score_word = 0
    if clean in positive:
        total_score_word += 1
    if clean in negative:
        total_score_word -= 1
    else:
        total_score_word += 0
    return total_score_word

def sentiment_of_text(text:str)->int:
    """
    sentiment_of_text returns a score based on positive or negative words for a string
    if word doesn't exist on positive or negative it's considered neutral
    """
    positive = load_positive_words()
    negative = load_negative_words()
    # calls cleanup function
    clean = cleanup(text)
    # split str into a list (for loop)
    words = clean.split(" ")
    total_score = 0
    for word in words:
        if word in positive:
            total_score += 1
        if word in negative:
            total_score -= 1
        else:
            total_score += 0
    return total_score
