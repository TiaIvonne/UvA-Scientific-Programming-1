# First or Last Year 

year = int(input("Enter a year: "))
flag = 100

if year % flag == 1:
    print(year, 'is the first year of the century!')
elif year % flag == 0:
    print(year, 'is the last year of the century!')
else:
    print(year, 'is neither the first nor last year of the century.')






