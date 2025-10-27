# Odd number list exercise
# Ivonne Mendoza

number = int(input("Enter a positive number: "))
# Start with empty list
accumulator = []
# Save first element
accumulator.append(number)
odd_list = []


# First while validate there are no zero numbers or negative in the list and ends loop
while number > 0:
    number = int(input("Enter a positive number: "))
    if number > 0:
        accumulator.append(number)

# After saves all numbers in a list, looping over and extract only odd numbers
for i in accumulator:
    # solo para checks
    # print(i)
    if i % 2 == 1:
        odd_list.append(i)

print(f'The list {accumulator} contains these odd numbers {odd_list}.')
