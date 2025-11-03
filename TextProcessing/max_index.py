# Max
# Ivonne Mendoza
# ivonne@imendoza.io


def max_index(lst: list)-> int:
    if len(lst) > 0:
        # Other solution is set the accumulator with an infinite range
        # https://flexiple.com/python/python-infinity
        # accumulator = float('-inf')
        indice = 0
        # Necesito trabajar con los indices asi que uso range(len())
        for i in range(1,len(lst)):
            if lst[i] >= lst[indice]:
                indice = i
        return indice
    else:
        return None

# Call the function

lst = []
max_index(lst)






