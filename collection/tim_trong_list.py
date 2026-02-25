list_a =  [2,4,6,3,8,9]
x = int(input("Nhap gia tri tim kiem"))
# tim xem x co trong list hay khong
if x in list_a:
    print(f"tim thay {x} tai vi tri {list_a.index(x)}")
else:
    print(f"khong tim thay {x}")