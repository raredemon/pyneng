# -*- coding: utf-8 -*-
'''
Задание 4.5

Список VLANS это список VLANов, собранных со всех устройств сети,
поэтому в списке есть повторяющиеся номера VLAN.

Из списка нужно получить уникальный список VLANов,
отсортированный по возрастанию номеров.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]

vlan_set = set(VLANS)
vlan_list = list(vlan_set)
vlan_list.sort()
print(vlan_list)

[1, 2, 3, 4, 10, 20, 30, 100]