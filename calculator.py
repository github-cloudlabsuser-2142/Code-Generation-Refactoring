class Calculator:
    def add(self, x, y):
        return x + y
        
    def subtract(self, x, y):
        return x - y
        
    def multiply(self, x, y):
        return x * y
        
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

def main():
    calc = Calculator()
    print(calc.add(10, 5))      # 15
    print(calc.subtract(10, 5)) # 5
    print(calc.multiply(10, 5)) # 50
    print(calc.divide(10, 5))   # 2.0

if __name__ == "__main__":
    main()