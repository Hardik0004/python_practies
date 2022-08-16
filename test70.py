list1 = [1,3, 6, 9, 10, 15, 18, 21]
list2 = [2,4, 8, 16, 20, 24, 28]
res = list()

import pdb
pdb.set_trace()

odd_listnumber = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_listnumber)

even_listnumber = list2[0::2]
print("Element at even-index positions from list two")
print(even_listnumber)

print("Printing Final list")
res.extend(odd_listnumber)
res.extend(even_listnumber)
print(res)
