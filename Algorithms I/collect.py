# collect
# Ivonne Mendoza
# ivonne@imendoza.io

# Pregunta antes de entrar al loop
number = float(input("How much change is owed?: "))
# Guarda el number en un temp
temporal = number
negative_number = False

# Keep asking while number is negative
while number < 0:
    number = float(input("How much change is owed?: "))
    # Saves again in a temp variable
    temporal = number
    if number >= 0:
        negative_number = False
    else:
        negative_number = True

if negative_number == True:
    print(f'You should return these coins []')
else:
    # Do calculations outside the while loop
    new_number = round(temporal * 100)
    new_int = int(new_number)
    # Coin definitions
    coins = [25,10,5,1]
    # Save coins
    purse = 0
    res2 =[]
    for i in range(len(coins)):
        # coins[i] valor dentro de la lista no el indice 0,1.2 etc
        # Calculates total coins for each iteration
        purse = new_int // coins[i]
        # See coins needed just for testing
        #print(f'total coins {purse} of {coins[i]}')
        # Calculates remainder an updates new_int for next iteration
        new_int = new_int % coins[i]
        # See next number for iteration
        #print(f'Next number for calculations {new_int}')
        # Another loop inside purse
        for j in range(purse):
            res2.append(coins[i])
    print(f'You should return these coins: {res2}')
