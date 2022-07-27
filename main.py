from employee import Employee
from department import Department


def create_employee(first_name: str, last_name: str, age: int, job: str, salary: float) -> Employee:
    return Employee(first_name, last_name, age, job, salary)


def apply_bonus_to_employee(employee: Employee, bonus: float):
    employee.apply_bonus(bonus)


def create_department(name: str) -> Department:
    return Department(name)


def remove_department(department: Department):
    pass


def apply_bonus_to_every_employee(department: Department):
    pass


def add_employee_to_department(employee: Employee, department: Department):
    pass


def remove_employee_from_department(employee: Employee, department: Department):
    pass


if __name__ == '__main__':
    pass
