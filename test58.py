def string_balance(s1, s2):

    flag = True

    for char in s1:

        if char in s2:

            continue
        else:

            flag = False

    return flag

s1 = "nsuaP"

s2 = "Pansuriya"

flag = string_balance(s1, s2)

print("example 1 s1 and s2 are balanced:", flag)

s1 = "next"

s2 = "Panxt"

flag = string_balance(s1, s2)

print("example 2 s1 and s2 are balanced:", flag)
