
##In python Method overloading is not directly support. so here we use some trick


class student:
            
    def sum(self,a=None,b=None,c=None):
        s1=0
        if a!=None and b!=None and c!=None:
            s1=a+b+c
        elif a!=None and b!=None:
            s1=a+b
        else:
            s1=a 
        return s1

s=student()

print(s.sum(6,4))