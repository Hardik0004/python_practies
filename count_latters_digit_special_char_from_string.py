import pdb
pdb.set_trace()


def find_digits_chars_symbols(str):

    chars = 0
    digit = 0
    symbol_count = 0

    for char in str:
        if char.isalpha():
            chars += 1
        elif char.isdigit():
            digit += 1
        else:
            symbol_count += 1

    print("Chars =", chars, "Digits =", digit, "Symbol =", symbol_count)


str = "sdSMO@#893SDSdwsc"

print("total counts of chars, Digits, and symbols \n")
find_digits_chars_symbols(str)
