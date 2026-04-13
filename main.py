import math

def calculate_area(radius):
    # Intentional Code Smell: Unused variable
    pi_value = 3.14159 
    
    if radius < 0:
        # Intentional Logic Error: Returning a string instead of a number
        return "Invalid"
    
    return math.pi * (radius ** 2)

def process_data(items):
    # Intentional Code Smell: Using a 'bare' except block
    try:
        for i in range(len(items)):
            print(f"Processing item: {items[i]}")
    except:
        print("An error occurred")

if __name__ == "__main__":
    print(f"Area: {calculate_area(5)}")
    process_data(["apple", "banana", "cherry"])
