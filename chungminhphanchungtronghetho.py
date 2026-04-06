from sympy import symbols, Implies, Not, And
from sympy.logic.inference import satisfiable

# ==========================================
# KHAI BÁO BIẾN
# ==========================================
Spike, Overload, Cache, Hang = symbols('Spike Overload Cache Hang')

# ==========================================
# LUẬT
# ==========================================

# Luật 1: (Overload ∧ ¬Cache) → Hang
rule1 = Implies(And(Overload, Not(Cache)), Hang)

# Luật 2: Spike → Overload
rule2 = Implies(Spike, Overload)

# ==========================================
# SỰ THẬT
# ==========================================

fact1 = Spike
fact2 = Not(Cache)

# ==========================================
# KB (Cơ sở tri thức)
# ==========================================

KB = rule1 & rule2 & fact1 & fact2

print("KB:", KB)

# ==========================================
# PHẢN CHỨNG (Resolution)
# ==========================================

# Giả sử Hang là SAI
result = satisfiable(KB & Not(Hang))

print("-" * 30)

if result is False:
    print("Kết luận: Hệ thống sẽ bị TREO (Hang = True)")
else:
    print("Không suy ra được Hang")
    print("Trường hợp thỏa mãn:", result)