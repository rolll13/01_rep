print('Exc_1')
try:
    unit = int(input("Что во что переводим: байты в килобайты - 1,"
                 " килобайты в байты - 2 "))
except ValueError:
    print('Неверный выбор, попробуй еще')
else:
    if unit != 1 and unit != 2:
        print('Неверный выбор, попробуй еще')
    else:
        num = int(input('Введите число: '))
        if unit == 1:
            print(float(num/1024))
        else:
            print(float(num*1024))


print("Exc_2")

num = input("Введите число: ")
mult = 1
sum = 0
for i in num:
    sum += int(i)
    if i != 0:
        mult *= int(i)
    else:
        mult = 0
print('Сумма: ', sum, 'Произведение: ', mult)


print('Exc_3')

min_x=float(input('Минимальное значение x: '))
max_x=float(input('максимальное значение х: '))
step=float(input('Шаг: '))
x = min_x

while x <= max_x:
    y = -1.24 * x**2 + x
    print('Y = ', y, ' X = ', x)
    x += step
else:
    print('Конец')


print('Exc_4')

num = input('Введите число: ')
i = len(num)-1
j = 0
f = 0

while j < i :
    if num[j] == num[i]:
        j += 1
        i -= 1
        f =1
    else:
        f = 0
        print('Не палиндром')
        break
if f == 1:
    print('Палиндром')


print('Exc_5')

l = [1,-5,8,13]
len_l = len(l)
sum = 0

for i in l:
    if i > 0:
        sum += i
    else:
        len_l -= 1
        continue
print(sum/len_l)

