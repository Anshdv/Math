
nums = input('\nEnter a series of numbers separated by commas: ')
nums = nums.split(',')
print(nums)

total = 0
for num in nums:
    try: total += int(num)
    except ValueError: continue
average = total/len(nums)

print('\nThe average of the numbers you entered is', round(average, 2))
