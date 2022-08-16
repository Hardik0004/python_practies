import pdb
pdb.set_trace()

set1 = {26, 33, 42, 39, 40, 85, 55, 13, 53, 76, 23}
set2 = {24, 65, 76, 99, 26, 85, 14, 67, 42, 48}

print("First Set ", set1)
print("Second Set ", set2)

intersection = set1.intersection(set2)
print("Intersection is ", intersection)

for item in intersection:
    set1.remove(item)

print("First Set after removing common element ", set1)

for item in intersection:
    set2.remove(item)
print("second Set after removing common element ", set2)
