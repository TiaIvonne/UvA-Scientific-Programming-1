# Align
# Ivonne Mendoza
# ivonne@imendoza.io
# https://docs.vultr.com/python/standard-library/str/rjust



def right_align(text:str)->str:
    # Split by newline
    splitted_by_newline = text.split("\n")
   # Accumulator to register the max len
    max_c = 0
    # List for append aligned lines
    r_align = []
    # find maximym len for every line
    for line in splitted_by_newline:
        if len(line) > max_c:
            max_c = len(line)

    #with maximun we can use rjust()
    for lines in splitted_by_newline:
        r_align.append(lines.rjust(max_c))

    return "\n".join(r_align)








