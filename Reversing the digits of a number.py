input_number = int(input('\nEnter a number to reverse its digits. Do not enter to many digits or your answer will be wrong: '))
number = input_number
ans = ''
new_number = 1
while new_number != 0:
    ans += str(number % 10)
    new_number = int(number / 10)
    number = new_number
print(f'\nReversing the digits of {input_number} equals {ans}.')
