import math
n = int(input("nhap vao so nguyen"))
if n < 2:
    print("khong phai la so nguyen to")
elif n == 2:
    print("la so nguyen to.")
else:
    # kiem tra so nguyen to
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            print(f"khong phai so nguyen to")
            break
    else:
        print(f"{n} so nguyen to")