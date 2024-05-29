def calculate_bmi(weight, height):
    """Calculate the BMI given weight in kilograms and height in meters."""
    return weight / (height ** 2)  # BMI formula: weight divided by height squared

def classify_bmi(bmi):
    """Classify the BMI into categories."""
    if bmi < 18.5:  # BMI less than 18.5 is considered underweight
        return "Underweight"
    elif 18.5 <= bmi < 24.9:  # BMI between 18.5 and 24.9 is considered normal weight
        return "Normal weight"
    elif 25 <= bmi < 29.9:  # BMI between 25 and 29.9 is considered overweight
        return "Overweight"
    else:  # BMI 30 or higher is considered obesity
        return "Obesity"

def main():
    """Main function to execute the BMI calculator."""
    print("Welcome to the BMI Calculator")  # Greeting message
    try:
        weight = float(input("Please enter your weight in kilograms: "))  # Prompt user for weight
        height = float(input("Please enter your height in meters: "))  # Prompt user for height

        if weight <= 0 or height <= 0:  # Check if the input values are positive
            print("Weight and height must be positive numbers.")  # Error message for non-positive input
            return  # Exit the function if invalid input is detected

        bmi = calculate_bmi(weight, height)  # Calculate BMI using the weight and height
        category = classify_bmi(bmi)  # Determine the BMI category

        print(f"Your BMI is: {bmi:.2f}")  # Print the calculated BMI, formatted to 2 decimal places
        print(f"You are classified as: {category}")  # Print the BMI category

    except ValueError:  # Handle invalid input (non-numeric values)
        print("Invalid input. Please enter numerical values for weight and height.")  # Error message for invalid input

if __name__ == "__main__":
    main()  # Execute the main function if this script is run directly
