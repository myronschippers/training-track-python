# multi-deminsional array
travel_expenses = [
    [5.00, 2.75, 22.00, 0.00, 0.00],
    [24.75, 5.50, 15.00, 22.00, 8.00],
    [2.75, 5.50, 0.00, 29.00, 5.00],
]

# getting total number of items in a list
number_of_weeks = len(travel_expenses)
print("There are {} weeks worth of expenses".format(number_of_weeks))

# return week one from the travel_expenses list
week_1_expenses = travel_expenses[0]
print("All of week 1's expenses; ")
print(week_1_expenses)

# getting expenses for week one Tuesday
tuesday_week_1 = travel_expenses[0][1]
print("Tuesday expenses for Week 1 are {}\n".format(tuesday_week_1))

print("======> Tuesday Expenses for all Weeks:")
tuesday = 1
expense_last_index = len(travel_expenses) - 1
# creating the equivalent of the for i loop in JS
for week_index in range(len(travel_expenses)):
    tuseday_expense = travel_expenses[week_index][tuesday]
    line_break = ""
    if week_index == expense_last_index:
        line_break = "\n"
    print("Tuesday expenses for Week #{} are {} {}".format(week_index + 1, tuseday_expense, line_break))
    
print("======> Travel Expenses:")
week_number = 1
for week in travel_expenses:
    print("* Week #{}: ${}".format(week_number, sum(week)))
    week_number += 1
