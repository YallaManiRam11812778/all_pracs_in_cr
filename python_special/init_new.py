# init_new.py

#     __hash__
#     __init__
#     5 useful decorators in python indently
#     cache
#     retry
#     yeild
#     atexit
#     @staticmethod
#     @classmethod
#     def f(x:int): -> str|int|float|bool example

import atexit
class Vehicle:
    def __new__(self, wheels):
        self.wheels = wheels

        if self.wheels!=2 and self.wheels!=4:
            return super().__new__(self)
        elif self.wheels == 2:
            return bike(wheels)
        elif self.wheels == 4:
            return car(self.wheels)
        
    
    def __init__(self, wheels):
        print(f"There is no vehicle with these - {wheels} wheels.")
        print(self.oyo())
        
    def oyo(self):
        # raise Exception
        return f"Park ur auto which is having '{self.wheels}' - wheels...."
        
        
@atexit.register
def goodbye():
    print("GoodBye............")
    
class bike:
    def __init__(self, wheels) -> None:
        print(f"Bike delivered because ordered is {wheels} - wheels.")
    
class car:
    def __init__(self, wheels) -> None:
        print(f"Ordered vehicle with 4 wheels so booking a car with {wheels} - wheels.")

if __name__ == "__main__":
    Vehicle(3)
    Vehicle(2)
    Vehicle(4)

    if True:
        atexit.unregister(goodbye)