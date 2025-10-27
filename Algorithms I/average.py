# average
# Ivonne Mendoza
# ivonne@imendoza.io

'''
Write a program called average.py that calculates the average of a sequence of
positive numbers entered by the user.
'''

number = float(input("Enter a positive number: "))
# Start with empty list
accumulator = []
# Save first element
accumulator.append(number)
sum = 0


# First while validate there are no zero numbers or negative in the list and ends loop
while number > 0:
    number = float(input("Enter a positive number: "))
    if number > 0:
        accumulator.append(number)

# After saves all numbers in a list, looping over and extract only odd numbers
for i in accumulator:
    # suma todos los numeros del indice
    sum += i

# Calculates average
average = sum / len(accumulator)



print(f'The average of {accumulator} is {average}.')
