import pdb
pdb.set_trace()


def calculation(a, b):

    addition = a + b
    subtraction = a - b
    MULTIPLE = a*b
    division = a/b

    return ('The sum of number is ', addition,
            "The subtraction of number is,", subtraction,
            "The multification of number is ", MULTIPLE,
            "The divison of number is", division)


res = calculation(10, 10)
print(res)
