class HotBeverage:
    
    price = 0.30
    name = "hot beverage"
    
    def description(self):
        return "Just some hot water in a cup."

    def __str__(self):
        return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}"


class Coffee(HotBeverage):
    
    price = 0.40
    name = "coffee"
    
    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    
    price = 0.30
    name = "tea"
    

class Chocolate(HotBeverage):
    
    price = 0.50
    name = "chocolate"
    
    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    
    price = 0.45
    name = "cappuccino"
    
    def description(self):
        return "Un po' di Italia nella sua tazza!"

if __name__ == "__main__":
    
    hot_b = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappuccino = Cappuccino()

    print(hot_b)
    print()
    print(coffee)
    print()
    print(tea)
    print()
    print(chocolate)
    print()
    print(cappuccino)