
input_number = int(input('\nEnter a number of which you want to add its digits: '))
number = input_number
ans = 0
new_number = 1
while new_number != 0:
    ans += number % 10
    new_number = int(number / 10)
    number = new_number
print(f'\nAdding up the digits of {input_number} equals {ans}.')

# testing git
