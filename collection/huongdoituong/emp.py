from dataclasses import dataclass
@dataclass 
class Employee:
    name: str
    base_salary: float
    def calc_salary(self):
        return 0
    # @dataclass được định nghĩa là kiểu fill
@dataclass 
class FullTimeEmployee(Employee):
    bonus: float

    def calc_salary(self):
        return self.base_salary + self.bonus
@dataclass
class PartTimeEmployee(Employee):
    salary_per_h: float
    hour: int

    def calc_salary(self):
        return self.salary_per_h * self.hour
    
nv1 = FullTimeEmployee("An", 20_000,bonus=10_000)
nv2 = PartTimeEmployee("Binh", 0, 100,30)

print(nv1,nv1.calc_salary())
print(nv2,nv2.calc_salary())