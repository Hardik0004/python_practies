numbers_a = [1,2,3,4,5,1,]
numbers_b = [6,7,8,9,0,1,2]

def first_last_same(numberList):
    print("Given list:", numberList)
    
    import pdb
    pdb.set_trace()
    first_num = numberList[0]
    last_num = numberList[-1]
    
    if first_num == last_num:
        return True
    else:
        return False

print("result is", first_last_same(numbers_a))
print("result is", first_last_same(numbers_b))