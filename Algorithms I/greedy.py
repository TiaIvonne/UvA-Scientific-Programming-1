# greedy
# Ivonne Mendoza
# ivonne@imendoza.io

# Pregunta antes de entrar al loop
number = float(input(" "))
# Guarda el number en un temp
temporal = number
# Coin definitions
quarters = 25
dimes = 10
nickels = 5
cents = 1
coins = 0

# Keep asking while number is negative
while number < 0:
    number = float(input(" "))
    # Saves again in a temp variable
    temporal = number





# Do calculations outside the while loop
new_number = round(temporal * 100)
new_int = int(new_number)
#Calculates how many coins QUARTERS
# // int division
first = new_int // quarters
coins = first
remain_1 = new_int % quarters
# Calculates how many coins DIMES
second = remain_1 // dimes
# Accumulator for coins
coins =  coins + second
remain_2 = remain_1 % dimes
# Calculates how many coins NICKELS
third = remain_2 // nickels
coins = coins + third
remain_3 = remain_2 % nickels
# Calculates how many coins CENTS
fourth = remain_3 // cents
coins = coins + fourth

print(f'How much change is owed? {temporal}, {coins}')
