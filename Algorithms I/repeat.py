# Check repeat
# Ivonne Mendoza
# ivonne@imendoza.io

text = input("Enter text: ")
times = int(input("How many times?: "))


for i in range(times):
    # Si es i < times la condicion siempre se cumple y no pasa al else
    # i parte en 0
    if  i < times - 1:
        print(text, end = '')
    else:
        print(text)

