# the value in classmethod can directly accessed by class 
# we can use both self and cls but technically cls is correct in classmethod

class Company:
    company_name = "TCS"
    
    @classmethod
    def sound(cls):
        return cls.company_name

employee = Company
print(Company.sound())   # access using class method functionality
print(employee.sound()) # direct access using object