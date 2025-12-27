class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            if self.b == 0:
                return "Error: Division by zero is not allowed."
            return self.a / self.b
        else:
            return "Error: Invalid operation."

    def display_result(self):
        result = self.calculate()
        print("\nCalculation Result")
        print("-" * 25)
        print(f"First Number  : {self.a}")
        print(f"Second Number : {self.b}")
        print(f"Operation     : {self.operation.capitalize()}")
        print(f"Result        : {result}")
        print("-" * 25)


# ----------- User Input Section -----------
try:
    a = float(input("Enter first number (a): "))
    b = float(input("Enter second number (b): "))
    operation = input("Enter operation (add / subtract / multiply / divide): ")

    calc = Calculator(a, b, operation)
    calc.display_result()

except ValueError:
    print("Error: Please enter valid numeric values.")
