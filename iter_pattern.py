
#iteratore class is created and used to iterate over the elements of a collection.
#The iterator object returned by the iter() function is an iterator object.
class iterator:
    def __init__(self) -> None:
        self.n=0
        #iter funtion returns an iterator object
    def __iter__(self):
        return self

        #next() function returns the next item of an iterator.
    def __next__(self):
        if self.n<5:
            self.n+=1
            return self.n
        else:
            raise StopIteration
#it is object of iterator class
it=iterator()
#for loop is used to iterate over the elements of a collection.
for i in it:
    for j in range(i):
        print(j, end=' ')
    print()

