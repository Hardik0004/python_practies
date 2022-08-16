def merge_list(listodd,listeven):
    result_list=[]
    for num in listodd:
        if num %2 !=0:
            result_list.append(num)

    for num in listeven:
        if num %2 ==0:
            result_list.append(num)
            return result_list

listodd= [10,15,25,28,30]
listeven=[12,14,19,20,24]

print("result list",merge_list(listodd,listeven))