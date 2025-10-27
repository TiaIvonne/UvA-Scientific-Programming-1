# Sum until
# Ivonne Mendoza
number = int(input("Enter a positive number: "))
total = 0
last = 0

while number < 1:
    number = int(input("Try again: "))
for i in range(1, number + 1):
    if number > total:
        total += i
        last = i


print(f"The sum of all numbers from 1 to {last} is {total} (which is bigger or equal to {number}).")
