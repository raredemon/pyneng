# -*- coding: utf-8 -*-
'''
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

IP = '192.168.3.1'

# разбиваем переменную на 4 части, разделитель точка
oct1, oct2, oct3, oct4 = IP.split('.')

# описываем шаблон вывода
templ = '''
{0:<10} {1:<10} {2:<10} {3:<10}
{0:010b} {1:010b} {2:010b} {3:010b}
'''

# вывод
print(templ.format(int(oct1), int(oct2), int(oct3), int(oct4)))

#192        168        3          1
#0011000000 0010101000 0000000011 0000000001
