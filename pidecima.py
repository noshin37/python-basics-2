from decimal import Decimal, getcontext

def calculate_pi(decimal_places):
    getcontext().prec = decimal_places + 1  # Set precision (additional 1 for the integral part)
    pi_value = Decimal(22) / Decimal(7)  # A common approximation for pi
    return pi_value

# Example usage
desired_decimal_places = int(input("Enter the number of decimal places for pi: "))
pi_result = calculate_pi(desired_decimal_places)
print(f"Value of pi to {desired_decimal_places} decimal places:\n{pi_result}")