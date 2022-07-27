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
        self.total_salary += bonus

    def __str__(self):
        return (f"Name: {self.first_name + ' ' + self.last_name},\n" +
                f"Age: {self.age},\n" +
                f"Job: {self.job},\n" +
                f"Salary: {self.salary},\n" +
                f"Bonus: {self.bonus},\n" +
                f"Total salary: {self.total_salary}\n")

    def save_employee_to_txt(self):
        with open(f"{self.first_name}_{self.last_name}_{self.age}.txt", "w") as file:
            file.write(self.__str__())