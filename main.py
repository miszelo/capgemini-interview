from employee import Employee
from department import Department


def create_employee(first_name: str, last_name: str, age: int, job: str, salary: float) -> Employee:
    return Employee(first_name, last_name, age, job, salary)


def create_department(name: str, users: []) -> Department:
    return Department(name, users)


def apply_bonus_to_employee(employee: Employee, bonus: float):
    employee.apply_bonus(bonus)


def remove_department(department: Department):
    department.remove_department()


def apply_bonus_to_every_employee(department: Department, bonus: float):
    department.apply_bonus_to_every_employee(bonus)


def add_employee_to_department(employee: Employee, department: Department):
    department.add_employee_to_department(employee)


def remove_employee_from_department(employee: Employee, department: Department):
    department.remove_employee_from_department(employee)


if __name__ == '__main__':
    michal = create_employee("Michał", "Kawczak", 22, "Software Developer", 4000)
    john = create_employee("John", "Croft", 44, "HR", 8000)
    anna = create_employee("Anna", "Mucha", 39, "Accountant", 5000)
    tom = create_employee("Tom", "Cruise", 35, "Team Leader", 25000)
    capgemini = create_department("capgemini", [])

    capgemini.add_employee_to_department(michal)
    capgemini.add_employee_to_department(john)
    capgemini.add_employee_to_department(anna)
    capgemini.add_employee_to_department(tom)

    capgemini.display_employees()

    capgemini.apply_bonus_to_every_employee(300)
    capgemini.display_employees()

    capgemini.remove_employee_from_department(anna)
    capgemini.display_employees()

    michal.save_employee_to_txt()

    jacob = create_employee("Jacob", "Ken", 25, "Software Developer", 3000)
    kris = create_employee("Kris", "Tin", 33, "Team Leader", 15000)
    patrik = create_employee("Patrik", "Decula", 26, "Accountant", 4500)
    kasia = create_employee("Kasia", "Cichopek", 37, "HR", 3000)
    xyz_company = create_department("xyz", [jacob, kris, patrik, kasia])

    xyz_company.display_employees()

    jacob.apply_bonus(600)

    xyz_company.display_employees()

    xyz_company.display_departments()