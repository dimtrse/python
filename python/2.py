from math import log, tanh

a = float(input('A = '))
x = float(input('X = '))

print('======')
function = int(input('1 - G\n2 - F\n3 - Y\nFunction = '))

if function == 1:
	try:
		g = (7 * (20 * a ** 2 + 11 * a * x - 45 * x ** 2)) / (3 * a ** 2 - 7 * a * x + 4 * x ** 2)
		print('G = ' + str(g))
	except ValueError:
		print('Ошибка вычисления')
	except ZeroDivisionError:
		print('Деление на ноль :(')
elif function == 2:
	try:
		f = tanh(60 * a ** 2 + 88 * a * x + 21 * x ** 2)
		print('F = ' + str(f))
	except ValueError:
		print('Ошибка вычисления')
	except ZeroDivisionError:
		print('Деление на ноль :(')
elif function == 3:
	try:
		y = (log(-40 * a ** 2 + 3 * a * x + x ** 2 + 1)) / log(2)
		print('Y = ' + str(y))
	except ValueError:
		print('Ошибка вычисления')
	except ZeroDivisionError:
		print('Деление на ноль :(')
else:
	print('Введите корректное значение')

input("\n\nНажмите Enter чтобы выйти .")