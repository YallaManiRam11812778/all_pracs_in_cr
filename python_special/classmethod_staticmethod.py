# classmethod_staticmethod.py
class dollars_to_rupees:
    def __init__(self, original_dollars:int,_dollars:int=None):
        self.original_dollar = original_dollars
        self.dollars = _dollars
    
    def converting_to_rupees(self):
        print(f"converted {self.original_dollar}$ to {self.dollars}Rs")
        return f"converted {self.original_dollar}$ to {self.dollars}Rs"
    
    @classmethod
    def class_method_for_dollar(cls, _dollar:int):
        converterd_to_rupees : int = _dollar * 80
        return cls(_dollar,converterd_to_rupees)

if __name__ == '__main__':
    conversion = dollars_to_rupees.class_method_for_dollar(40)
