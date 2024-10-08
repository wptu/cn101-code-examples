# NUM_EMPLOYEES is used as a constant for the size of the list.
NUM_EMPLOYEES = 6

# Create a list to hold employee hours.
hours = [0] * NUM_EMPLOYEES

# Get each employee's hours worked.
for index in range(NUM_EMPLOYEES):
    prompt = f'Enter the hours worked by employee {index + 1}: '
    hours[index] = float(input(prompt))

# Get the hourly pay rate.
pay_rate = float(input('Enter the hourly pay rate: '))

# Display each employee's gross pay.
for index in range(NUM_EMPLOYEES):
    gross_pay = hours[index] * pay_rate
    print(f'Gross pay for employee {index + 1}: ${gross_pay:,.2f}')
