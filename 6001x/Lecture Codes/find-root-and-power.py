# Write a program that asks the user to enter an integer and prints
# two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer
# entered by the user. If no such pair of integers exists, it should print a message
# to that effect.
x = int(input('Enter a number: '))
# x = 9
root = 0
pwr = 1
while root < x:
    while pwr < 6:
        if root**pwr == x:
            break
        pwr += 1
    if root**pwr == x:
        break
    pwr = 1
    root += 1
if root**pwr == x:
    print('Root is', root, '& Power is', pwr, 'for', x)
else:
    print('No such pair of integers exists')
