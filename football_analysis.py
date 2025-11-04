# Practice read files
# Lee todo el archivo
input_file = open('VanBasten.txt','r')
'''
for line in input_file:
    print(line)
'''

total_goals = 0

# split by newline and save in a list
for line in input_file:
    split_data = line.split(',')

    season = int(split_data[0][0:4])
    goals = int(split_data[3])
    total_goals += goals

    if goals > 20:
        print(f"In {season} Van Basten scored > 20 goals, nl {goals}")


print(f"TOTAL: In total Van Basten scored {total_goals} clubgoals")
input_file.close()

