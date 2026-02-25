list_a = [1,2,3,4,6]
list_b = [x // 2 if x % 2 == 0 else x for x in list_a]
print(list_b)