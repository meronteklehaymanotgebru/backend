class Student:
    school="AkiraChix"
    def __init__ (self,first_name,last_name,age,country):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
        self.year=2025-age
        self.scores=[]
    def greet_student(self):
        return f"Hello{self.first_name}, welcome to {self.school}"
    def calculate_age(self):
        return self.year
    def initials(self):
        first=self.first_name[0]
        second=self.last_name[0]
        return first + second
    def add_score(self,score):
        self.scores.append(score)
        total=0
        for i in self.scores:
            total+=i
        return f"Your new total score is {total}"




   

    # name="Nebyat"
    # age=20
    # country="Ethiopia"


 #self refers to an instance of the class
     
#we don't use snake case in cllases they start with capital, we don't necessarily need brackets unless we are inheriting
#if we have 2 words in our claa we use camel case
# to create an object we need o intitiantiaze
#?? a method to convert them to a dictionary and acces the atributes