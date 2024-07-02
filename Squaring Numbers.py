numbers = []
squared_numbers = []
cubed_numbers = []
repeating = int(input('\nHow many numbers do you want to enter: '))
print('')
for in_x in range(repeating):
    input_number = int(input('Enter a number: '))
    numbers.append(input_number)
which = int(input('''\nDo you want the squares or the cubes of the numbers you entered.
Enter 2 for squares, 3 for cubes, and 1 for both: '''))
for number in numbers:
    squared_numbers.append(number ** 2)
for number in numbers:
    cubed_numbers.append(number ** 3)
if which == 1:
    print(f'\nThe squares of the numbers that you entered are {squared_numbers}.')
    print(f'The cubes of the numbers that you entered are {cubed_numbers}.')
elif which == 2:
    print(f'\nThe squares of the numbers that you entered are {squared_numbers}.')
elif which == 3:
    print(f'\nThe cubes of the numbers that you entered are {cubed_numbers}.')
