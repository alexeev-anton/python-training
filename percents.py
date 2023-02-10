def percentage(x, y):
    one_percent = y / 100
    res = x / one_percent
    return res


def print_result(x, y):
    print(str(x) + " is " + str(percentage(x, y)) + "% of " + str(y))


print_result(29, 200)
