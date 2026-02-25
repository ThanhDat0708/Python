a = [1,2,3,4,5,6,7,8,9,10]
b = a[::2]
# b = [x for x in b if not (x % 2)]
b = [x **2 for x in b]
print(a)
print(b)
