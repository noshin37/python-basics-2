from datetime import datetime

def days_since_birth(birthdate):
    # Get the current date
    current_date = datetime.now()

    # Convert the birthdate string to a datetime object
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

    # Calculate the difference in days
    days_difference = (current_date - birthdate).days

    return days_difference

# Example usage
birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
days_since_birth_result = days_since_birth(birthdate_str)
print(f"Days since birth: {days_since_birth_result} days")