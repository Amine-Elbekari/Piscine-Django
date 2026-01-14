import beverages
import random

class CoffeeMachine:
    
    def __init__(self):
        self.serving_count = 0

    def serve(self, drink_class):
        
        if self.serving_count >= 10:
            raise self.BrokenMachineException()
        self.serving_count += 1
        if random.randint(0, 1):
            return drink_class()
        return self.EmptyCup()

    def repair(self):
        self.serving_count = 0
        
    class EmptyCup(beverages.HotBeverage):
        
        name = "empty cup"
        price = 0.90
        
        def description(self):
             return "An empty cup?! Gimme my money back!"
    
    class BrokenMachineException(Exception):
        
        def __init__(self, message="This coffee machine has to be repaired."):
            super().__init__(message)


if __name__ == "__main__":
    
    m1 = CoffeeMachine()
    for i in range(25):
        try:
            res = m1.serve(beverages.Tea)
            print(f"{i}: {res}")
        except CoffeeMachine.BrokenMachineException as e:
            print(f"\nError:{e}")
            m1.repair()
            print()
        