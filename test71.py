list1 = [23,45,76,34,99,72,61,40,90]

import pdb
pdb.set_trace()

print("Original list ", list1)
element = list1.pop(4)
print("List After removing element at index 4 ", list1)

list1.insert(2, element)
print("List after Adding element at index 2 ", list1)

list1.append(element)
print("List after Adding element at last ", list1)