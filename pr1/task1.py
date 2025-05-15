print('Введите J: ')
J = str(input())
print('Введите S: ')
S = str(input())
count = 0
for i in S:
    if i in J:
        count += 1
print('Вывод: ',count)