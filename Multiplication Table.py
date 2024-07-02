num = int(input("\nWhat number's multiplication table do you want: "))
factor = int(input('\nUntil what number do you want it: '))
print()
for counter in range(1, factor + 1):
    print(f'{num} x {counter} = {num * counter}')
