def sum_up_diagonals(lst):
    sum1 = 0
    sum2 = 0
    for a in range(len(lst)):
        sum1 = sum1 + lst[a][a]
        sum2 = sum2 + lst[a][-a-1]

    return sum1+sum2

list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
print(sum_up_diagonals(list1))