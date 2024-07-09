n = int(input('Введите число от 3 до 20: '))

if 3 <= n <= 20:
    password = ""
else:
    print('Число должно быть от 3 до 20!')
    exit()

for i in range(1, n):
    for j in range(i + 1, n):
        if (i + j) % n == 0:
            password += str(i)
            password += str(j)

print(f'Пароль для числа {n}: {password}')


