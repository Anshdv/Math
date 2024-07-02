numbers = []
repeating = int(input('How many numbers do you want to enter: '))
for in_x in range(repeating):
    input_number = int(input('Enter a number: '))
    numbers.append(input_number)
evens = 0
odds = 0
even_list = []
odd_list = []
for number in numbers:
    if number % 2 == 0:
        evens += 1
        even_list.append(number)
    else:
        odds += 1
        odd_list.append(number)
print(f'''\nThere are {evens} even numbers and {odds} odd numbers.
The even numbers are {even_list} and the odd numbers are {odd_list}.''')
