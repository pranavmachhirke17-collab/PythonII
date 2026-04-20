class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age        

    def person_info(self):
        print("Name:",self.name)
        print("Age:",self.age)

class employee:
    def __init__(self,employee_id,salary):
        self.employee_id=employee_id
        self.salary=salary

    def employee_info(self):
        print("Employee ID:",self.employee_id)
        print("Salary:",self.salary)

class manager(person,employee):
    def __init__(self,name,age,employee_id,salary,department):
        person.__init__(self,name,age)
        employee.__init__(self,employee_id,salary)
        self.department=department

    def manager_info(self):
        print("Department:",self.department)
    
    def display_all(self):
        self.person_info()
        self.employee_info()
        self.manager_info()
        
    
values = manager("ABC", 21 , "XY0454","₹99,000", "CS" )

values.display_all()