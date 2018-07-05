# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

vlan1 = command1.strip().split()[-1]
vlan2 = command2.strip().split()[-1]
list1 = list(vlan1.split(','))
list2 = list(vlan2.split(','))
set1 = set(list1)
set2 = set(list2)
print(set1 & set2)

#Out[9]: {'1', '100', '3'}