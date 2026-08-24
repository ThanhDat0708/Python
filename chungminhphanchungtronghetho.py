from sympy import symbols, Implies, Not, And
from sympy.logic.inference import satisfiable

# not là phép phủ định, and là phép hội, implies là phép kéo theo
# satisfiable là hàm kiểm tra tính thỏan mãn của một biểu thức logic
Spike, Overload, Cache, Hang = symbols('Spike Overload Cache Hang')

# spike: sự kiện có nhiều người truy cập cùng lúc
# overload: hệ thống bị quá tải
# cache: hệ thống có bộ nhớ đệm để giảm tải
# hang: hệ thống bị treo


# Luật 1: (Overload ∧ ¬Cache) → Hang
#  Nếu hệ thống bị quá tải và không có bộ nhớ đệm thì sẽ bị treo
rule1 = Implies(And(Overload, Not(Cache)), Hang)

# Luật 2: Spike → Overload
# Nếu có nhiều người truy cập cùng lúc thì hệ thống sẽ bị quá tải
rule2 = Implies(Spike, Overload)

# Các sự kiện spike đúng và hệ thống không có bộ nhớ đệm

fact1 = Spike
fact2 = Not(Cache)


#  ghép tất các dự kiện lại với nhau tạo thành một hệ thống tri thức lớn
KB = rule1 & rule2 & fact1 & fact2

print("KB:", KB)

# nếu kết quả trả về là False thì hệ thống sẽ bị treo, ngược lại nếu trả về một mô hình thỏa mãn thì không suy ra được Hang
# Giả sử Hang là SAI
result = satisfiable(KB & Not(Hang))
#  30  dấu gạch ngang để phân tách kết quả cho dễ nhìn
print("-" * 30)

if result is False:
    print("Kết luận: Hệ thống sẽ bị TREO (Hang = True)")
else:
    print("Không suy ra được Hang")
    print("Trường hợp thỏa mãn:", result)