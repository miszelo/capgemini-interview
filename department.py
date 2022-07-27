class Department:
    departments = []
    users = []

    def __init__(self, name: str):
        self.name = name
        self.departments.append(self.name)

    def display_employees(self):
        pass

    def display_departments(self):
        pass
