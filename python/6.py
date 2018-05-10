from math import log, tanh

a = float(input('A = '))
x = float(input('минимальное значнеие X = '))
x_max = float(input('максимальное значнеие X = '))

if x > x_max:
    exit('Минимальное значение не может быть меньше максимального')

step = int(input('Шаги = '))
step_value = float(input('Размер шага = '))

results = {'G': [], 'F': [], 'Y': []}

for i in range(0, step):
    try:
        g = (7 * (20 * a ** 2 + 11 * a * x - 45 * x ** 2)) / (3 * a ** 2 - 7 * a * x + 4 * x ** 2)
        results['G'].append(g)
        # print('G = ' + str(g))
    except ValueError:
        print('Ошибка вычисления')
    except ZeroDivisionError:
        print('На ноль делить нельзя')

    try:
        f = tanh(60 * a ** 2 + 88 * a * x + 21 * x ** 2)
        results['F'].append(f)
        # print('F = ' + str(f))
    except ValueError:
        print('Ошибка вычисления')
    except ZeroDivisionError:
        print('На ноль делить нельзя')

    try:
        y = (log(-40 * a ** 2 + 3 * a * x + x ** 2 + 1)) / log(2)
        results['Y'].append(y)
        # print('Y = ' + str(y))
    except ValueError:
        print('Ошибка вычисления')
    except ZeroDivisionError:
        print('На ноль делить нельзя')

    x += step_value
    if x >= x_max:
        exit('X > X_MAX')

print('=== G ===')
print(results['G'])
print('=== F ===')
print(results['F'])
print('=== Y ===')
print(results['Y'])

input("\n\nНажмите Enter чтобы выйти .")