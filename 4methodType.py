
class student:
    #static/class variable
    name="swapnil"
    school="Excellarate"

    def __init__(self, m1,m2,m3) -> None:
        #instance variable
        self.m1=m1
        self.m2=m2
        self.m3=m3
    #instance method
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    @classmethod
    def get_student_info(cls):
        return 'name of the student is {}, and school name is {}'.format(cls.name, cls.school)

    @staticmethod
    def info():
        print('This is Class info from Excellarate univerce')


s1=student(45,35,65)

#to call static method use class name .(dot) method name
student.info()
print( s1.get_student_info())
print(s1.avg())

