from employee import Employee


class Department:
    departments = []

    def __init__(self, name: str, employees: []):
        self.name = name
        self.employees = employees
        self.departments.append(self.name)

    def display_employees(self):
        print(f"Employees of {self.name}:")
        for employee in self.employees:
            print(employee)

    def display_departments(self):
        print("Departments:")
        for department in self.departments:
            print(department)

    def add_employee_to_department(self, employee: Employee):
        self.employees.append(employee)

    def remove_employee_from_department(self, employee: Employee):
        self.employees.remove(employee)

    def apply_bonus_to_every_employee(self, bonus: float):
        for employee in self.employees:
            employee.apply_bonus(bonus)

    def remove_department(self):
        self.departments.remove(self)

    def __iter__(self):
        return self

