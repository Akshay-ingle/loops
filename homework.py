def power(base, exponent):
    """Calculates the power of a number."""
    return base ** exponent

def main():
    print("Welcome to the Power Calculator!")
    
    try:
        # Input the base number
        base = float(input("Enter the base number: "))
        
        # Input the number of calculations
        n = int(input("How many power calculations do you want to perform? "))
        if n <= 0:
            print("The number of calculations should be a positive integer!")
            return
        
        # Perform n calculations
        for i in range(1, n + 1):
            try:
                exponent = int(input(f"Enter the exponent for calculation {i}: "))
                result = power(base, exponent)
                print(f"{base} raised to the power of {exponent} is: {result}")
            except ValueError:
                print("Invalid input for exponent. Skipping this calculation.")
        
        print("All calculations are done!")
    
    except ValueError:
        print("Invalid input! Please enter numeric values for the base and an integer for the number of calculations.")

# Run the program
if __name__ == "__main__":
    main()
