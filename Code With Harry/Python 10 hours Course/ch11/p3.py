class Employee:
    salary = 234 # in LPA
    increment = 20 # Increment is in %

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment / 100)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, val):
        self.increment = (val / self.salary - 1)* 100
        return self.increment
    
a = Employee()
print(type(a))
print(a.salary)
print(a.salaryAfterIncrement)
print(a.increment)