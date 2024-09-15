fuel_type = input()
fuel_litrs = float(input())




if fuel_type == 'Gas':
    if fuel_litrs >= 25:
        fuel_type = 'gas'
        print(f"You have enough {fuel_type}.")

    else:
        fuel_type = 'gas'
        print(f"Fill your tank with {fuel_type}!")

elif fuel_type == 'Diesel':
    if fuel_litrs >= 25:
        fuel_type = 'diesel'
        print(f"You have enough {fuel_type}.")

    else:
        fuel_type = 'diesel'
        print(f"Fill your tank with {fuel_type}!")

elif fuel_type == 'Gasoline':
    if fuel_litrs >= 25:
        fuel_type = 'gasoline'
        print(f"You have enough {fuel_type}.")
    else:
        fuel_type = 'gasoline'
        print(f"Fill your tank with {fuel_type}!")

else:
    print(f"Invalid fuel!")