# Max exercise
# Ivonne Mendoza
# ivonne@imendoza.io


def max(lst: list)-> int:
    if len(lst) > 0:
        # Other solution is set the accumulator with an infinite range
        # https://flexiple.com/python/python-infinity
        # accumulator = float('-inf')
        accumulator = lst[0]
        for i in lst:
            if i >= accumulator:
                accumulator = i
        return accumulator
    else:
        return None

# Call the function

lst = []
max(lst)






