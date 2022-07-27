class Employee:
    def __init__(self, first_name: str, last_name: str, age: int, job: str, salary: float):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.salary = salary
        self.bonus = 0
        self.total_salary = self.salary + self.bonus

    def apply_bonus(self, bonus: float):
        self.bonus = bonus
