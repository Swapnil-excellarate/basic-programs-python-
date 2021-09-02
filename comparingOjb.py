class compare:
    #step 1 is create a init method 
    def __init__(self) -> None:
        self.age=20
    #step 3 is create a function/method and define two variable 1st is slef(object it_self) ND 2ND is other
#object 
    def compares(self, other):
        if self.age == other.age:
            return True
        else:
            return False

c1=compare()
# it optional, If you not assign value 30 then it will automatically take same age(20) which is define 
# in init method
c1.age=30
c2=compare()
# step2 try to compare the 2 object but compare function is inbuild so we have to create a function
if c1.compares(c2):
    print('they are same')
else:
    print('They are differnt')