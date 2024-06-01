# Employee Hierarchy: Create an employee hierarchy (e.g., Employee, Manager, Executive)
# where each employee type has common attributes (e.g., name, ID, salary) and specific attributes/methods.
# Implement polymorphic methods such as calculating salary for each employee type.
class Employee:
    """
    Base class for all employees.

    Attributes:
    - name: employee's name.
    - ID: unique employee identifier.
    - salary: base salary of the employee.
    """

    def __init__(self, name, ID, salary):
        self.name = name
        self.ID = ID
        self.salary = salary

    def calc_compensation(self):
        """Calculate the total compensation for an employee (base salary)."""
        return self.salary

    def __str__(self):
        return f"Employee: {self.name}, ID: {self.ID}, Salary: ${self.salary:,.2f}"


class Manager(Employee):
    """
    Class representing a manager.

    Additional attributes:
    - work_hours: number of hours worked per week.
    - bonus: a bonus based on additional responsibilities.
    """

    def __init__(self, name, ID, salary, work_hours, bonus):
        super().__init__(name, ID, salary)
        self.work_hours = work_hours
        self.bonus = bonus

    def calc_compensation(self):
        """Calculate the total compensation for a manager (base salary + bonus)."""
        return self.salary + self.bonus

    def __str__(self):
        return f"Manager: {self.name}, ID: {self.ID}, Salary: ${self.salary:,.2f}, Bonus: ${self.bonus:,.2f}"


class Executive(Employee):
    """
    Class representing an executive.

    Additional attributes:
    - stock_options: value of the stock options.
    """

    def __init__(self, name, ID, salary, stock_options):
        super().__init__(name, ID, salary)
        self.stock_options = stock_options

    def calc_compensation(self):
        """Calculate the total compensation for an executive (base salary + stock options)."""
        return self.salary + self.stock_options

    def __str__(self):
        return f"Executive: {self.name}, ID: {self.ID}, Salary: ${self.salary:,.2f}, Stock Options: ${self.stock_options:,.2f}"


# Example Usage
emp = Employee("John Doe", "E123", 50000)
mgr = Manager("Jane Smith", "M456", 60000, 40, 10000)  # Base salary with bonus
exec = Executive("Alice Johnson", "X789", 80000, 30000)  # Base salary with stock options

print(emp)
print("Total Compensation:", emp.calc_compensation())

print("\n" + str(mgr))
print("Total Compensation:", mgr.calc_compensation())

print("\n" + str(exec))
print("Total Compensation:", exec.calc_compensation())
