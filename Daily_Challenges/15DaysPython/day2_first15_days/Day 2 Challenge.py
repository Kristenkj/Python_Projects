name = input('What is your name?')
sales = float(input('How much have you sold this month?'))

total_sales = (sales * .13)
total_sales = round(total_sales, 2)
print(f"{name} is entitled to ${total_sales} in commissions this month")
