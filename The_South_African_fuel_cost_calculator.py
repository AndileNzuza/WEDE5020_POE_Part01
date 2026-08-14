#Calculate fuel costs
kilometers_estimate = float(input("Enter the amount of kilometers you wish to travel: "))
current_petrol_price = float(input("Enter the current petrol price: "))
liters_needed = kilometers_estimate / 10
total_cost = liters_needed * current_petrol_price
formatted_cost = round(total_cost, 2)
print(f"The cost of your fuel cost adds up to {formatted_cost}.")