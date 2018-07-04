# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3[<32;89;11M
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
value = ospf_route.split()
value.remove('O')
value.insert(0,'OSPF')
ip_template = '''
Protocol:           {}
Prefix:             {}
AD/Metric:          {}
Next-Hop:           {}
Last update:        {}
Outbound Interface: {}
'''
proto, prefix, metric, via, gw, uptime, interface = value
print(ip_template.format(proto, prefix, metric.strip('[]'), gw.strip(','), uptime.strip(','), interface))
