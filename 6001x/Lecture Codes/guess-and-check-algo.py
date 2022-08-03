# cube = 27
# for guess in range(abs(cube)+1):
#     if guess**3 >= abs(cube):
#         break
# if guess**3 != abs(cube):
#     print(cube, 'is not a perfect cube')
# else:
#     if cube < 0:
#         guess = -guess
#     print('Cube root of '+str(cube)+' is '+str(guess))

# x = int(input('Enter an interger: '))
# ans = 0
# while ans**3 < abs(x):
#     ans = ans + 1
# if ans**3 != abs(x):
#     print(x, 'is not a perfect cube')
# else:
#     if x < 0:
#         ans = -ans
#     print('Cube root of', x, 'is', ans)

# Exercise 3.2
# Write a program that asks the user to enter an integer and prints
# two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer
# entered by the user. If no such pair of integers exists, it should print a message
# to that effect.
# x = int(input('Enter a number: '))
# # x = 9
# root = 0
# pwr = 1
# while root < x:
#     while pwr < 6:
#         if root**pwr == x:
#             break
#         pwr += 1
#     if root**pwr == x:
#         break
#     pwr = 1
#     root += 1
# if root**pwr == x:
#     print('Root is', root, '& Power is', pwr, 'for', x)
# else:
#     print('No such pair of integers exists')

# Exercise
# Let s be a string that contains a sequence of decimal numbers
# separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints the
# sum of the numbers in s.
# total = 0
# s = '1.23,2.4,3.123'
# for c in s:
#     if c != '.' and c != ',':
#         total += int(c)
# print(total)

x = 0.0
for i in range(10):
    x = x + 0.1
if x == 1.0:
    print(x, '= 1.0')
else:
    print(x, 'is not 1.0')

# 10011 = 1*1 + 1*2 + 0*4 + 0*8 + 1*16 = 1 + 2 + 16 = 19
