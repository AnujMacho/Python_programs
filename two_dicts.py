def two_list_dictionary(keys, values):
    return {keys[i]: values[i] if i < len(values) else None for i in range(len(keys))}


print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))