numbers = []
repeated_numbers = []
repeating = int(input('\nHow many numbers do you want to enter in a list (you can enter zero and negative numbers): '))
for in_x in range(repeating):
    input_number = int(input('Enter a number: '))
    if input_number not in numbers:
        numbers.append(input_number)
    else:
        repeated_numbers.append(input_number)
positives = 0
negatives = 0
positive_list = []
negative_list = []
for number in numbers:
    if number > 0:
        positives += 1
        positive_list.append(number)
    elif number < 0:
        negatives += 1
        negative_list.append(number)
for number in repeated_numbers:
    if number > 0:
        positives += 1
    elif number < 0:
        negatives += 1
word_1 = 'are'
word_2 = 'numbers'
if positives == 1:
    word_1 = 'is'
    word_2 = 'number'
elif positives == 0:
    positives = 'no'
print(f'''\nThere {word_1} {positives} positive {word_2} and {negatives} negative numbers.
The positive numbers are {positive_list} and the negative numbers are {negative_list}. The repeated numbers were {repeated_numbers}.''')
for number in numbers:
    if number == 0:
        print('\nZero is one of the numbers you entered and it does not fall into either the positive or negative category.')
