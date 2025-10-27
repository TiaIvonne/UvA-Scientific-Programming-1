# Leap years for loop

year1 = int(input("Enter a year: "))
year2 = int(input("Enter a year 2: "))


for year in range(year1, year2):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, 'is a leap year!')
    else:
        print(year, 'is not a leap year.')
