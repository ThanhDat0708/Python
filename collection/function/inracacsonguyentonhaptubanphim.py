import math
def is_prime_number(num: int) -> bool:
    """Nếu là số nguyên tố thì return true, không phải snt thì return false"""
    if num < 2:
         return False
    elif  num == 2:
        return True
    else:
        #  kiểm tra số nguyên tố 
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0: 
                return False
    return True
# Nhập dữ liệu
n = int(input("Nhập vào số nguyên tố: "))

for i in range(2,n+1):
    if is_prime_number(i):
            print(i)