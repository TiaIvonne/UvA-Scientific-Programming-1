# Align
# name: Ivonne Mendoza email: ivonne@imendoza.io
# This code aligns some text to the right
# source: https://docs.vultr.com/python/standard-library/str/rjust


def right_align(text:str)->str:
    """
    This function takes a left align string and returns the same text but aligned to the right.
    Example:
    This text is left aligned.
    Lets change that.

    return:
    This text is left aligned.
         Lets change that.
    """
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








