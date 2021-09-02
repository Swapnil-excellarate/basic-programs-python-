class computer:
    def config(self):
        print('8gb, 1Tb, HP')

# here create a varible and assign the class to that veriable
comp1=computer()
comp2=computer()

#here we calling the config fuction with the comp1 and comp2 variable 
computer.config(comp1)
computer.config(comp2)

#This is the right way to calling function config
#here we use direct variavble name with function name to call function
comp1.config()
comp2.config()