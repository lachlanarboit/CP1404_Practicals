for i in range(1, 21, 2):
    print(i, end=' ')
print()

for j in range (0, 100, 10):
    print(j, end=' ')
print()

for k in range(20, 1, -1):
    print(k, end=' ')
print()

number_stars = int(input("Number of Stars: "))
print("Star Formation")
for i in range(number_stars):
    print('*', end = ' ')