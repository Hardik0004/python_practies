import pdb
pdb.set_trace()

list1 = [" Hello ", " take "]
list2 = [" dear ", " care "]

res = [x + y for x in list1 for y in list2]
print(res)
