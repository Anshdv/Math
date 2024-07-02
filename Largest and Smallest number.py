number_list = []
how_many_numbers = int(input('\nHow many numbers do you want to enter: '))
which_number = 0
for in_x in range(how_many_numbers):
    which_number += 1
    number = int(input(f'Enter number {which_number}: '))
    number_list.append(number)
counter = 0
greater_number = number_list[counter]
for in_x in range(how_many_numbers - 1):
    counter += 1
    if greater_number > number_list[counter]:
        greater_number = greater_number
    else:
        greater_number = number_list[counter]
print(f'\nThe greatest number of the numbers you entered was {greater_number}.')
small_number = input('\nDo you want to know the smallest number (say "yes" or "no"): ')
if small_number == 'yes':
    counter = 0
    smallest_number = number_list[counter]
    for in_x in range(how_many_numbers - 1):
        counter += 1
        if smallest_number < number_list[counter]:
            smallest_number = smallest_number
        else:
            smallest_number = number_list[counter]
    print(f'\nThe smallest number of the numbers you entered was {smallest_number}.')
else:
    print('OK. See you later!')
