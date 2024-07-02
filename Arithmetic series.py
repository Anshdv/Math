starting_number = int(input('''\nEnter a number you want your arithmetic series to start with.
Do not go over one million: '''))
ending_number = int(input('''\nEnter a number you want your arithmetic series to end with.
Do not go over one million: '''))
answer = 0
if starting_number != ending_number:
    while ending_number >= starting_number:
        answer += ending_number
        ending_number -= 1
    print(f'\nThe sum of this arithmetic series is {answer}.')
else:
    print('\nThe numbers you entered are the same. Enter to different numbers to make an arithmetic series.')

