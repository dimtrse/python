from math import log, tanh

a = float(input('A = '))
x = float(input('Минимальное  значение X = '))
x_max = float(input('Максимальное значение X = '))

if x > x_max:
    exit('Минимальное значение не может быть меньше максимального')

step = int(input('Шаги = '))
step_value = float(input('Размер шага = '))

print('======')
function = int(input('1 - G\n2 - F\n3 - Y\nФункция = '))

result_values = []

for i in range(0, step):
    if function == 1:
        selected_function = 'G'
        try:
            g = (7 * (20 * a ** 2 + 11 * a * x - 45 * x ** 2)) / (3 * a ** 2 - 7 * a * x + 4 * x ** 2)
            result_values.append(g)
            # print('G = ' + str(g))
        except ValueError:
            print('Ошибка вычисления')
        except ZeroDivisionError:
            print('Деление на ноль')
    elif function == 2:
        selected_function = 'F'
        try:
            f = tanh(60 * a ** 2 + 88 * a * x + 21 * x ** 2)
            result_values.append(f)
            # print('F = ' + str(f))
        except ValueError:
            print('Ошибка вычисления')
        except ZeroDivisionError:
            print('Деление на ноль')
    elif function == 3:
        selected_function = 'Y'
        try:
            y = (log(-40 * a ** 2 + 3 * a * x + x ** 2 + 1)) / log(2)
            result_values.append(y)
            # print('Y = ' + str(y))
        except ValueError:
            print('Ошибка вычисления')
        except ZeroDivisionError:
            print('Деление на ноль')
    else:
        exit('Введите корректное значение')

    x += step_value
    if x >= x_max:
        exit('Значение X > X_MAX')

print('============== РЕЗУЛЬТАТЫ ================')
print(*result_values)

print('============== ИНФОРМАЦИЯ ==============')
print('MIN VALUE IN FUNCTION ' + selected_function + '= ' + str(min(result_values)))
print('MAX VALUE IN FUNCTION ' + selected_function + '= ' + str(max(result_values)))

print('========== ПОИСК ============')
search_str = float(input('Введите значение для поиска = '))
print('Результат:', result_values.count(search_str))

print('========== Четные числа ===========')
number = int(input('ЧИСЛО = '))
even_count = 0

while number > 0:
    if number % 2 == 0: even_count += 1
    number = number // 10
print('КОЛИЧЕСТВО = ', even_count)

input("\n\nНажмите Enter чтобы выйти .")