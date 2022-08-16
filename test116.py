tuple1 = (('a', 32), ('b', 44), ('c', 12), ('d', 31))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))

print(tuple1)