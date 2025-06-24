# property_methods.py
class HRMS:
    def __init__(self, employee):
        self._emp_name = employee
    
    @property
    def employees(self):
        print(f"Employees are - {self._emp_name}")
        return self._emp_name
    
    @employees.setter
    def employees(self, employee_name):
        print(f"Employee name changed to {employee_name}")
        self._emp_name = employee_name

    @employees.deleter
    def employees(self):
        print(f"Deleted Employee Permanently - {self._emp_name}")
        del self._emp_name

if __name__ == "__main__":
    emp = HRMS
    # emp.employees
    emp.employees = "john"
    emp.employees
    # del emp.employees
    # emp.employees = "parthiv"