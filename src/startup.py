from src.company import Company

class StartUp(Company):
    def __init__(self, name, address, num_employees):
        super().__init__(name, address)
        self.num_employees = num_employees

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_num_employees(self):
        return self.num_employees

    def __str__(self):
        return f'Name, {self.get_name()}, address, {self.get_address()}, num_employees, {self.get_num_employees()}'