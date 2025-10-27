# Sum exercise
# Ivonne Mendoza
# ivonne@imendoza.io


def sum(a:int, b:int)-> int:
    accumulator = 0
    for i in range(a,b+1):
        accumulator += i
    print(f' The sum of all numbers from {a} to {b} is {accumulator}.')

# Input section
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

# Call the function
sum(a, b)






