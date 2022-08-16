tuple1 = (12, 32)
tuple2 = (34, 54)

print(" old value to tuple 1:-", tuple1)
print(" old value to tuple 2:-", tuple2)

tuple1,tuple2 = tuple2,tuple1

print("new value to tuple 1:-", tuple1)
print("new value to tuple 2:-", tuple2)
