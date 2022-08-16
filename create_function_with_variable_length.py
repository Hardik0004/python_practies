import pdb
pdb.set_trace()


def func(*args):
    print("The value is :-")

    for i in args:

        print(i)


func(20, 40, 60, 80, 100)
func(10, 30, 50, 70, 90)
func(1, 11, 22, 33, 44, 55, 66, 77, 88, 99)
