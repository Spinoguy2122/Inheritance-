import math

class Shape:
    
    def __init__(self, name="Generic Shape"):
        self.name = name

    def calculate_area(self):
        
        raise NotImplementedError("Subclasses must implement calculate_area() method")

    def calculate_perimeter(self):
       
        raise NotImplementedError("Subclasses must implement calculate_perimeter() method")

    def display_info(self):
       
        try:
            area = self.calculate_area()
            perimeter = self.calculate_perimeter()
            print(f"\n--- {self.name} Calculation Result ---")
            print(f"Area: {area:.2f}")
            print(f"Perimeter: {perimeter:.2f}")
            print("------------------------------------")
        except NotImplementedError as e:
            print(f"Error: {e} for {self.name}. Cannot calculate information for a generic shape.")
        except ValueError as e:
            print(f"Error during calculation for {self.name}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {self.name}: {e}")

class Rectangle(Shape):
   
    def __init__(self, length, width):
        super().__init__("Rectangle") 
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive values.")
        self.length = length
        self.width = width

    def calculate_area(self):
        
        return self.length * self.width

    def calculate_perimeter(self):
       
        return 2 * (self.length + self.width)

class Square(Rectangle):
   
    def __init__(self, side):
       
        super().__init__(side, side)
        self.name = "Square" 
        self.side = side 

   

class Circle(Shape):
    
    def __init__(self, radius):
        super().__init__("Circle")
        if radius <= 0:
            raise ValueError("Radius must be a positive value.")
        self.radius = radius

    def calculate_area(self):
       
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
       
        return 2 * math.pi * self.radius



def get_positive_float_input(prompt):
   
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Input must be a positive number. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def main_calculator():
    
    print("--- Welcome to the Geometric Shape Calculator! ---")

    while True:
        print("\nSelect a shape to calculate:")
        print("1. Rectangle")
        print("2. Square")
        print("3. Circle")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        current_shape = None
        try:
            if choice == '1':
                length = get_positive_float_input("Enter the length of the rectangle: ")
                width = get_positive_float_input("Enter the width of the rectangle: ")
                current_shape = Rectangle(length, width)
            elif choice == '2':
                side = get_positive_float_input("Enter the side length of the square: ")
                current_shape = Square(side)
            elif choice == '3':
                radius = get_positive_float_input("Enter the radius of the circle: ")
                current_shape = Circle(radius)
            elif choice == '4':
                print("Thank you for using the calculator. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
                continue

            if current_shape:
                current_shape.display_info()

        except ValueError as e:
            print(f"Error: {e}. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")


if __name__ == "__main__":
    main_calculator()
