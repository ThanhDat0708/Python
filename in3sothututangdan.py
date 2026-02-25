a = int(input("Nhập a:"))
b = int(input("Nhập b:"))
c = int(input("Nhập c:"))
# if a<=b <= c:
#         print(f"kết quả {a},{b},{c}")
# elif a<=c<=b:
#         print(f"kết quả {a},{c},{b}")
# elif b<=a<=c:
#         print(f"kết quả {b},{a},{c}")
# elif b<=c<=a:
#         print(f"kết quả: {b},{c},{a}")
# elif c<=a<=b:
#         print(f"kết quả {c},{a},{b}")
# else:
#         print(f"kết quả {c},{b},{a}")
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print(f"3 so tang dan: {a},{b},{c}")
