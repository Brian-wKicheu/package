def hello():
    print(f"Hello Brian !")
    
class Greet:
    
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name
    
    def greet(self):
        return f"Hello there, my name is {self.name}"
    
