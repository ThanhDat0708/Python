a = int(input("Nhập a:"))
b = int(input("Nhập b:"))
c = int(input("Nhập c:"))
if a<=b and a<=c:
    if b<=c:
        print(f"kết quả {a},{b},{c}")
    else:
        print(f"kết quả {a},{c},{b}")
elif b<=a and b<=c:
    if a<=c:
        print(f"kết quả {b},{a},{c}")
    else:
        print(f"kết quả: {b},{c},{a}")
else:
    if a<=b:
        print(f"kết quả {c},{a},{b}")
    else:
        print(f"kết quả {c},{b},{a}")

    