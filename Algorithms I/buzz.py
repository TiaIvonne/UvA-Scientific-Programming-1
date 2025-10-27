# Buzz exercise

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

for x in range(first, second):
    if x % 5 == 0:
        print("buzz")
    else:
        print(x)


