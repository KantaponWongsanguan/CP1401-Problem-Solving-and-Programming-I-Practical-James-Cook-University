for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):  # a
    print(i, end=' ')
print()

for i in range(20, 0, -1):  # b
    print(i, end=' ')
print()

number_of_stars = int(input("Number of stars: "))  # c
for i in range(number_of_stars):
    print('*', end='')
print()

for i in range(1, number_of_stars + 1):  # d
    print('*' * i)
print()
