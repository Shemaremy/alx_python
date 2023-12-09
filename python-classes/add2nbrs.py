class Flacko:                        #Creating a class as usual
    def __init__ (self,a,b):         #Always a constructor must be created and exactyly like this with self
       self.a = n                    #Initialising a with value to be passed from outside the class
       self.b = m

    def add(self):
       return self.a + self.b

n = 10  
m = 12

callflacko = Flacko(m,n)
print(callflacko.add())