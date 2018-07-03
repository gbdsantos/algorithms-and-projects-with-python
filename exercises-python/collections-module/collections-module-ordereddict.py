from collections import OrderedDict

d = {}

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

d

for k, v in d.items():
    print(k, v)

d = OrderedDict()

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

d

for k, v in d.items():
    print(k, v)

