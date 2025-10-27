# Newton's method exercise
# Ivonne Mendoza
# ivonne@imendoza.io


n = float(input("Enter a number: "))
current_guess = n

for i in range(50):
    # math formula's
    # 0.5 * (25 + (25 / 25)) -> 13
    # 0.5 * (13 + (25 / 13)) -> 7.46
    new_guess = 0.5 * (current_guess + n / current_guess)
    # store the result of calculation to current_guess
    # example, first new_guess result is 13 and that's the current number now
    current_guess = new_guess
print(current_guess)



