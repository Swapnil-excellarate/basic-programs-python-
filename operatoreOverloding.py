class student:
    def __init__(self, m1,m2) -> None:
        self.m1=m1
        self.m2=m2
    #you have same method name but the arrgument is channge
    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        m3= student(m1,m2)

        return m3

s1=student(21,12)
s2=student(11,23)
# here we call plus operate so basically we call __add__() funtion. 
add=s1+s2

print(add.m2)