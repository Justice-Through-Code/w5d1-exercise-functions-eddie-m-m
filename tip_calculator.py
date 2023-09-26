# tip_calculator.py

# TODO: Create a function named calculate_tip
def tip_calculator():
    try:  # DO NOT MODIFY

        # TODO:
        # Get these user inputs
        # total_cost (float): The cost of the meal (without tax)
        # num_people (int): The number of people splitting the bill
        # tip_percentage (float): The tip percentage
        total_cost = float(input('What was the cost of the meal? '))
        num_people = int(input('How many people are splitting the bill? '))
        tip_percentage = float(input('What is the tip percentage? '))

    # TODO:
        # Calculate the total bill including tip and sales tax (10%).
        # Convert to float: The total bill (including tip and sales tax).

    # NOTE: Calculate the tip and tax separately.
        tip_amount = total_cost * (tip_percentage / 100)
        tax_amount = total_cost * .1
        total_bill = float(total_cost + tip_amount + tax_amount)
    # TODO:
        # Calculate how much each person should pay.
        # Convert to float: The amount each person should pay.
        amount_per_person = float(total_bill / num_people)
    # TODO:
        # Using an f-string, print two different statements
        # Total bill: $0.00
        # Each person should pay: $0.00
        print(
            f'Total bill: ${total_bill:.2f}\nEach person should pay: ${amount_per_person:.2f}')
    # NOTE: The amounts are displayed with 2 decimals only

    except:  # TODO: modify this except to include a Built-in Exception
        # TODO: Print an statement telling the user their input is invalid
        print('Your input is invalid.')


if __name__ == "__main__":  # DO NOT MODIFY
    tip_calculator()  # DO NOT MODIFY
