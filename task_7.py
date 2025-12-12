def sum_digits(digits):
    int_list = [int(item) for item in digits]
    return sum(int_list)

def digit_root(num):
    split_str = list(str(num))

    while len(split_str) > 1:
        split_str = str(sum_digits(split_str))

    return int(split_str)

digit_root(3789)