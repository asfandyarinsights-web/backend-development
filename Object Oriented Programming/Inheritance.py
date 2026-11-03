class Employees:
    def __init__(self, name, lastname):
        self.name=name
        self.lastname=lastname

class Supervisors(Employees):
        def __init__(self,name,lastname,password):
            super().__init__(name,lastname)
            self.password=password
            
class Chefs(Employees):
    def leave_request(self,days):
        return "May I take a leave for "+str(days)+"Days"


adrian=Supervisors("Adrian","A","appple")
johnathan=Employees("Johnathan","J")


emily=Chefs("emily","12345")
print(adrian.password)
print(emily.name)

print(emily.leave_request(3))

