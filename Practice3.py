# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = int(input("Введите любое число: "))
num = str(n)
nn = num + num
nnn = num + num + num
summa = n + int(nn) + int(nnn)

print("Результат: {0}+{1}+{2}={3}".format(n, nn, nnn, summa))
