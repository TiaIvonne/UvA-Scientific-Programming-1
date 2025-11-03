# Resplit
# Ivonne Mendoza
# ivonne@imendoza.io


def resplit(text:str):
    temp_text = text.replace(".",",")
    replaced_text = temp_text.split(",")
    result = []
    temporal = []
    for every_word in replaced_text:
        # Strip adds an empty character by the end of the text
        # see temporal array for checks
        temp = every_word.strip()
        #temporal.append(temp)
        #print(f'string temporal {temporal}')
        # Only adds 'real strings' not empty
        if temp != "":
            result.append(temp)
    return result






