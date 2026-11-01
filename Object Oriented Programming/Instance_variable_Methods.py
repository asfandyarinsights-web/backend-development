class Employee:

    def __init__(self,name, paid,salary):
        self.name=name
        self.paid=paid
        self.salary=salary

    def pay(self):
        self.paid=True

    def status(self):
        if self.paid==True:
            print(f'{self.name} has paid Salary is : {self.salary}')
        else:
            print(f'{self.name} has not been paid')


nathan=Employee("Nathan",True,5000)
roger=Employee("Roger",False,5000)

nathan.status()
roger.status()

roger.pay()

roger.status()
