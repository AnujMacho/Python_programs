def find_greater_numbers(l1):
    count = 0
    for i in range(len(l1)):
        for j in range(i+1, len(l1)):
            if l1[i] < l1[j]:
                count += 1
    return count

print(find_greater_numbers([1,2,3]))
print(find_greater_numbers([6,1,2,7]))
print(find_greater_numbers([5,4,3,2,1]))