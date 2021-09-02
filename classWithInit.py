class computer: 
    # Create a init method with the 3 variables 1st is object, 2nd and 3rd is cpu and ram  
    # here self mean the object it self, here you can see the 3 variable this are mention above  
    def __init__(self, cpu, ram) -> None: 
        self.cpu=cpu 
        self.ram=ram 
    
    #created the config function to display the behaviare. 
    def config(self):
        print('Config is', self.cpu, self.ram)

# here we create a object of the class and passing the values for cpu and ram 
comp1=computer('i5', '8gb') 
comp2=computer('i3', '16gb') 

#calling the function/method
comp1.config()
comp2.config()

