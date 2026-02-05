a = int(input("Nhập a:"))
b = int(input("Nhập b:"))
c = int(input("Nhập c:"))
if a>b | b<a | a>c:
    max = a
    print(f"{max} là số lớn nhất")
elif b>a | b>c:
    max = b
    print(f"{max} là số lớn nhất")
else:

    print(f"{c}là số lớn nhất")