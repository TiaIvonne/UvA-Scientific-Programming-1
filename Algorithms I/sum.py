# Sum

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

# Accumulator
total = 0 

for x in range(first, second + 1):
    total = total + x
print(f'The sum of all numbers from {first} to {second} is {total}.')


