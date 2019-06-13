def two_oldest_ages(lst):
    high_number = 0
    less_high_num = 0
    for a in lst:
        if a >high_number:
            high_number = a
    lst.remove(high_number)
    for a in lst:
        if a > less_high_num:
            less_high_num = a
    return [less_high_num, high_number]

print(two_oldest_ages([1, 2, 10, 8]))