
### Outer class
class car:
    ## init method to crate a instance vatiable
    def __init__(self, windows, door) -> None:
        self.windows=windows
        self.door=door

        #here we create object of inner class 
        self.car_info=self.car_engine() 

    ## Intance method 
    def info(self):
        print(self.windows, self.door)
        
        ##here we call the intance method of inner class
        self.car_info.show()
    
    # Inner class 
    class car_engine:
        # init method 
        def __init__(self) -> None:
            self.name='Audi'
            self.engine_type='petrol'
            self.model='A8'
        # instance method of inner class
        def show(self):
            print(self.name, self.engine_type, self.model)

# object class    
car1=car(4, 'windows')

car1.info()
