def trip_calculator():

    miles = int(input("Miles one-way = "))
    miles_gallon = int(input("Miles per gallon of vehicle = "))
    gallons = miles/miles_gallon

    price_gallon_start = float(input("Price per gallon at starting location = "))
    gas_going = price_gallon_start * gallons

    price_gallon_destination = float(input("Price per gallon at destination = "))
    gas_returning = price_gallon_destination * gallons

    gas = gas_going + gas_returning

    print("""
    Press 1 to calculate by night.
    Press 2 to calculate by week.
    Press 3 to calculate by month.
    """)
    m = int(input(" "))
    if m == 1:
        cost_per_night = int(input("Cost per night = "))
        number_of_nights = int(input("Number of nights = "))
        lodging = cost_per_night * number_of_nights
    elif m == 2:
        cost_per_week = int(input("Cost per week = "))
        number_of_weeks = int(input("Number of weeks = "))
        lodging = cost_per_week * number_of_weeks
    else:
        cost_per_month = int(input("Cost per month = "))
        number_of_months = int(input("Number of months = "))
        lodging = cost_per_month * number_of_months
    total_cost = gas + lodging
    print("Trip Expenses:")
    print("Gas = ${}".format(gas))
    print("Lodging = ${}".format(lodging))
    print("Total = ${}".format(total_cost))

trip_calculator()
