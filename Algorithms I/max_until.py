# Sum until
# Ivonne Mendoza\
# ivonne@imendoza.io

number = int(input("Enter a positive number: "))
# This saves the first number entered
accumulator = number

# Mientras el numero no sea 0 entra al loop y sigue preguntando
# Si es 0 termina el loop
# Mientras corre el loop sigue preguntando por numberos hasta que ingrese 0,
# en el acumulador va guardando cada numero ingresado mientras sea mayor al
# numero actual

while number > 0:
    number = int(input("Enter a positive number: "))
    if number >= accumulator:
        accumulator = number

print(f'The biggest number you entered was {accumulator}.')
#print(f'debug {accumulator}, {number}')
