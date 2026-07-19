# #create student class that take name and marks of 3 subjects as arguments in constructor.
# THen create a method to print the average

class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def avg(self):
        sum = 0
        for i in self.marks :
            sum += i
        print(f"Hello , {self.name}. Your Average is: {sum/3}")
        
s1 = Student("Darpan",[98,97,96])
s1.avg()
        

