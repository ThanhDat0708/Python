n = int(input("Nhập N:"))
tong = 0
for i in range(n):
    print(i)
    if i % 2 == 0:
        tong += i
    
print(f"tong tu 1 den n:{n},tong:{tong}")
    