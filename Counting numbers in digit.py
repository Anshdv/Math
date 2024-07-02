number = int(input('\nEnter a number of which you want to count its digits: '))
input_number = number
if number != 0:
    new_number = 1
    counter = 0
    while new_number != 0:
        new_number = int(number / 10)
        number = new_number
        counter += 1
    print(f'\nThe number of digits in {input_number} is {counter}.')
else:
    print('\nEnter a number that is not 0.')
