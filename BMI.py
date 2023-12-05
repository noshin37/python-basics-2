
def calculate_bmi(weight_kg, height_m):
    """
    Calculate BMI (Body Mass Index) using weight in kilograms and height in meters.
    Formula: BMI = weight (kg) / (height (m) * height (m))
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")
    
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI results based on commonly used categories.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Example usage
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi_result = calculate_bmi(weight, height)
interpretation = interpret_bmi(bmi_result)

print(f"Your BMI is: {bmi_result:.2f}")
print(f"Interpretation: {interpretation}")