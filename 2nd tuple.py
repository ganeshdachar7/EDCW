x = [("a", 3), ("b", 1), ("c", 2)]

def get_second_value(t):
    return t[1]

x_sorted = sorted(x, key=get_second_value, reverse=True)

print(x_sorted)