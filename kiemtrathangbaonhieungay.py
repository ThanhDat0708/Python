month = int(input("Nhập tháng: "))
if month in (1,3,5,7,8,10,12):
    print(f"tháng {month} có 31 ngày")
elif month in(4,6,9,11):
    print(f"tháng {month} có 30 ngày.")
elif month == 2:
    print(f"tháng {month} có 28 ngày.")
else:
    print(f"Vui lòng nhập lại")
    