class Person:
    def __init__(self, fname, lname,specialization):
        self.specialization = specialization
        self.firstname = fname
        self.lastname = lname
    def print_name(self):
        print(self.firstname,self.lastname)
class Runner(Person):
    def __init__(self,fname, lname,specialization,distance):
        super().__init__(fname,lname,specialization)
        # Person.__init__(self, fname, lname)
        self.distance = distance

class Dancer(Person):
    pass

runner = Runner("Михаил","Петров",'бегун',"спринт")
runner.print_name()
print(runner.distance)

