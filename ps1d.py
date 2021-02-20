monthly_salary = float(input("Enter your monthly salary:"))
total_cost = float(input("Enter the cost of the dream car:"))
percentage_car_increase = float(input("Enter the increase in the car's price, as a decimal:"))
percentage_salary_increase = float(input("Enter the percentage salary raise, as a decimal:"))


interest_rate = .01
epsilon = 150
low_percentage = 0
high_percentage = 10000.0
up_check = False
total_cost_temp = total_cost
current_savings = 0
number_of_steps = 0
guess_percentage = (high_percentage + low_percentage) / 2
while abs(current_savings - total_cost_temp) >= epsilon:
    if guess_percentage == 10000.0:
        up_check = True
        break
    current_savings = 0
    total_cost_temp = total_cost
    monthly_salary_temp = monthly_salary
    monthly_saved = monthly_salary * (guess_percentage / 10000.0)
    for month in range(0, 24):
        if month != 0 and month % 12 == 0:
            total_cost_temp += total_cost_temp * percentage_car_increase
        if month != 0 and month % 6 == 0:
            monthly_salary_temp += monthly_salary_temp * percentage_salary_increase
            monthly_saved = monthly_salary_temp * (guess_percentage / 10000.0)
        current_savings += monthly_saved + (current_savings * interest_rate)
    if current_savings < total_cost_temp:
        low_percentage = guess_percentage
    else:
        high_percentage = guess_percentage
    guess_percentage = (high_percentage + low_percentage) / 2
    number_of_steps += 1


if up_check:
    print("It is not possible to buy the car in two years")
else:
    print("The best saving rate:", "{:.3f}".format(guess_percentage / 10000))
    print("The number of steps in bisection search:", number_of_steps)
