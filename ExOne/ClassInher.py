class Employee:
    def __init__(self, FirstName, LastName, JobTitle, Salary, Email):
       self.FirstName = FirstName
       self.LastName = LastName
       self.JobTitle = JobTitle 
       self.Salary = Salary
       self.Email = Email
       self.RaiseAmount = 5
    def GiveRaise(self):
        self.Salary = self.Salary*self.RaiseAmount/100 + self.Salary
class Sales(Employee):
    def __init__(self, FirstName, LastName, JobTitle, Salary, Email, PhoneNumber):
        super().__init__(FirstName, LastName, JobTitle, Salary, Email)
        self.PhoneNumber = PhoneNumber
    def FollowUpEmail(self, name):
        print(f"Dear {name}, Thank you for your interest in our product. Please let me know if you have any questions. My email is {self.Email} or my phone number is {self.PhoneNumber}. Thanks, {self.FirstName} {self.LastName}")
class Development(Employee):
    def __init__(self, FirstName, LastName, JobTitle, Salary, Email):
        super().__init__(FirstName, LastName, JobTitle, Salary, Email)
    def Code(self):
        print(f"{self.FirstName} {self.LastName} is writing code")

Anthony = Sales("Anthony", "Ordaine", "Sales", 50000, "AnthonyOrdaine@Urmom.com", "1(234)-(567)-(8910)")

Anthony.FollowUpEmail("Dudeguy")
Anthony.FollowUpEmail("DudetGirl")
Anthony.GiveRaise()
print(Anthony.Salary)
Jon = Development("Jon", "Doe", "Development", 100000, "JonDoe@beepboop.com")
Jon.Code()
Jon.GiveRaise()
print(Jon.Salary)
