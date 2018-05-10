import numpy
import time

def calculation(x, y):
    for key in x:
        key_x = (key - centr_x)**2
        result_x.append(key_x)
    for key in y:
        key_y = (key - centr_y)**2
        result_y.append(key_y)
    result = list(map(lambda a, b: a + b, result_x, result_y))
    enter = 0
    not_enter = 0
    for key in result:
        if key <= radius**2:
            enter += 1
        else:
            not_enter += 1
    print('Входит или лежит на окружности точек = ', enter, '\nНе входит = ', not_enter)
    print('Центр окружности = ', centr_x, ';', centr_y)
    print('Точек всего = ', point_count)

def point_search(x, y):
    global os_y
    global os_x
    point_count_x = float(input('Введите координату поиска X = '))
    start = time.time()
    for key in x:
        if key == point_count_x:
            os_x.append(key)
    print('На этой координате найдено точек = ', len(os_x))
    len_x = len(os_x)
    if len(os_x) != len(y):
        os_y = os_y[:len_x]
    end = time.time()
    times.append(end - start)
    print('Время выполнения поиска точек = ', *times)

centr_x = float(input('Координата Х для центра окружности = '))
centr_y = float(input('Координата Y для центра окружности = '))
radius = float(input('Радиус = '))
point_count = int(input('Количество точек = '))
times = []

x = numpy.random.random_integers(-49, 49, point_count)
y = numpy.random.random_integers(-49, 49, point_count)

result_x = []
result_y = []
calculation(x, y)
os_x = []
os_y = y

while radius > 0:
    point_search(x, y)
    exit_prog = input('Выйти из программы  (y/n)')
    if 'y' in exit_prog:
        break

# тут пишем время выполнения в файл
times = str(times)
file = open('time.txt', 'w')
file.write(times)
file.close()

input("\n\nНажмите Enter чтобы выйти .")