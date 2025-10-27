# Positive number list exercise
# Ivonne Mendoza

number = int(input("Enter a number: "))
# Start with empty list
accumulator = []
# Save first element
accumulator.append(number)

while number > 0:
    number = int(input("Enter: "))
    if number > 0:
        accumulator.append(number)
print(f'My positive number list: {accumulator}')
