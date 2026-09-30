class Employee:
    company_name="TechCorp Solutions"
    total_employees=0
    pf_percentage=12.0
    MIN_SALARY=15000
    MAX_SALARY=50000

    def __init__(self, emp_id, name, department, salary, pan_number):
        self._emp_id=emp_id
        self.name=name
        self._department=department
        self.__pan_number=pan_number

        #use setter bcs we have to check whether its crct or not
        self.salary=salary
        # Why not using self bcs we want to increment for employee class not for current employee person
        Employee.total_employees+=1

    @property # behaves like a varaible
    def emp_id(self):
        return self._emp_id

    @emp_id.setter
    def emp_id(self,value):
        raise AttributeError("Employee id cannot be changed")

    @property
    def salary(self):
        return self._salary 

    @salary.setter
    def salary(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError("Salary must be a number")
        if value<Employee.MIN_SALARY or value>Employee.MAX_SALARY:
            raise ValueError(f"Salary must be between {Employee.MIN_SALARY} ans {Employee.MAX_SALARY}")
        self._salary=value

    def apply_hike(self,percent):
        if percent<0 or percent>50:
            raise ValueError("Hike percentage must be betwee 0 and 50")
        self.salary=self.salary+(self.salary*percent/100)
        return self.salary
    
    def calculate_pf(self):
        return self.salary*Employee.pf_percentage/100

    def transfer_department(self,new_dept):
        old=self._department
        self._department=new_dept
        return f"{old}->{new_dept}"

    #@classmethod is used when the method works with class variables instead of object variables. It receives cls (the class) as the first parameter.
    @classmethod
    def get_total_employees(cls):
        return cls.total_employees

    #@staticmethod is used for utility methods that do not need access to either instance variables (self) or class variables (cls).
    @staticmethod
    def is_valid_salary(amount):
        return Employee.MIN_SALARY<=amount <= Employee.MAX_SALARY

    def __str__(self):
        return (f"ID={self.emp_id}, " f"Name={self.name}," f"Department={self._department}," f"salary={self.salary}")