a = int(input("Nhập vào số a: "))
b = int(input("Nhập vào số b: "))
# co kha nang loi 
try:
    if b == 0:
        raise ValueError("Không thể chia cho 0")
    
    c = a / b
    print(f"Kết quả của {a} chia cho {b} là: {c}")
except ValueError as ex:
    print(ex)