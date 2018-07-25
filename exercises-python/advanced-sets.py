s = set()

s.add(1)
s.add(2)
s

s.add(2)
s

s.clear()
s

s = {1, 2, 3}
sc = s.copy()

sc
s.add(4)
s
sc

s.difference(sc)

s1 = {1, 2, 3}
s2 = {1, 4, 4}

s1.difference_update(s2)
s1

s
s.discard(2)
s

s1 = {1, 2, 3}
s2 = {1, 2, 4}
s1.intersection(s2)

s1 = {1, 2}
s2 = {1, 2, 3}
s3 = {5}

s1.isdisjoint(s2)
s1.isdisjoint(s3)
s1.issubset(s2)
s1.issuperset(s2)

s1.symmetric_difference(s2)
s1.union(s2)
s1.update(s2)


