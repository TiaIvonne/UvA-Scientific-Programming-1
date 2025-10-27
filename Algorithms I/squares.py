# Squares
# Ivonne Mendoza

'''
Write a program called average.py that calculates the average of a sequence
of positive numbers entered by the user
'''

number = float(input("Enter a positive number: "))
# Start with empty list
accumulator = []
# Save first element
accumulator.append(number)
square_list = []


# First while validate there are no zero numbers or negative in the list and ends loop
while number > 0:
    number = float(input("Enter a positive number: "))
    if number > 0:
        accumulator.append(number)

# After saves all numbers in a list, looping over and extract only odd numbers
for i in accumulator:
    # suma todos los numeros del indice
    i = i ** 2
    square_list.append(i)

print(f'The squares of {accumulator} are {square_list}.')
