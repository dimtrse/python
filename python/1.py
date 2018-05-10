from math import log, tanh

a = float(input('A = '))
x = float(input('X = '))

g = (7 * (20 * a ** 2 + 11 * a * x - 45 * x ** 2)) / (3 * a ** 2 - 7 * a * x + 4 * x ** 2)
f = tanh(60 * a ** 2 + 88 * a * x + 21 * x ** 2)
y = (log(-40 * a ** 2 + 3 * a * x + x ** 2 + 1)) / log (2)

print('=============')
print('G = ' + str(g))
print('F = ' + str(f))
print('Y = ' + str(y))

input("\n\nНажмите Enter чтобы выйти .")