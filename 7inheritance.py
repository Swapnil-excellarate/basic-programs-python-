class A:
    def feature1(self):
        return'feature 1 is working'
    
    def feature2(self):
        print('feature 2 is working')

class B(A): # if I want to inherite Class A then the syntax is class B(A):
    def feature3(self):
        print('feature 3 is working')
    
    def feature4(self):
        print('feature 4 is working')

# till this it is single inheritance one I create the one more and try to inherita both the class A & B thn it is 
# multiple inherit 

class C(B): #its multi-level inheritance, here class C inherite class B and class B inherite class A 
    def feature5(self):
        print('frature 5 is working')
        

b1=B()
C1=C()
C1.feature2()