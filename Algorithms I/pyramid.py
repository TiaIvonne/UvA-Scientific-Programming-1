number = int(input("Enter a positive number: "))
temp = number

# Keep asking while number is negative
while number < 0 or number > 23:
    number = int(input("Enter a positive number: "))
    # Saves again in a temp variable
    temp = number

# 3 loops
# First loop
# number = 3 so range 2, 3 + 2 range(2,5) -> 2,3,4
for i in range(2, temp + 2):
    # Second loop add double spaces to the pyramid
    # 1, 3 - i(2) + 2 range(1, 3)
    # segunda vuelta
    for j in range(1, temp - i + 2):
        print("  " , end ='')
        # test
        #print("a", end = '')
    # third loop to add the hash
    #range(1,3)
    for k in range(1, i + 1):
        print("# ", end = '')
    print()
