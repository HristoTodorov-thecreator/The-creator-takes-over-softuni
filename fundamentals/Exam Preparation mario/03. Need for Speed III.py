number_of_cars_obtained = int(input())

cars = []
kms = []
allfuel = []




for i in range(number_of_cars_obtained):
    car ,km,fuel= input().split('|')
    cars.append(car)
    kms.append(int(km))
    allfuel.append(int(fuel))

while True:
    command = input()
    if command == 'Stop':
        break
    splitted = command.split(' : ')
    firstcommand = splitted[0]
    if firstcommand == 'Drive':
        givencar = splitted[1]
        givendistance = int(splitted[2])
        givenfuel = int(splitted[3])
        carindex = cars.index(givencar)
        if allfuel[carindex] >= givenfuel:
            allfuel[carindex] -= givenfuel
            kms[carindex] += givendistance
            print(f"{givencar} driven for {givendistance} kilometers. {givenfuel} liters of fuel consumed.")
            if kms[carindex] >= 100000:
                cars.remove(givencar)
                allfuel.pop(carindex)
                kms.pop(carindex)
                print(f"Time to sell the {givencar}!")



        else:
            print(f'Not enough fuel to make that ride')


    if firstcommand == 'Refuel':
        givencar = splitted[1]
        givenfuel = int(splitted[2])
        carindex = cars.index(givencar)
        maxfuel = 75
        if allfuel[carindex] + givenfuel > maxfuel:

            print(f"{givencar} refueled with {maxfuel - allfuel[carindex]} liters")
            allfuel[carindex] = maxfuel


        else:
            allfuel[carindex] += givenfuel
            print(f"{givencar} refueled with {givenfuel} liters")



    if firstcommand == 'Revert':
        givencar = splitted[1]
        givenkms = int(splitted[2])
        carindex = cars.index(givencar)
        kms[carindex] -= givenkms
        if kms[carindex] < 10000:
            kms[carindex] = 10000
        else:
            print(f"{givencar} mileage decreased by {givenkms} kilometers")


for s in range(len(cars)):
    print(f"{cars[s]} -> Mileage: {kms[s]} kms, Fuel in the tank: {allfuel[s]} lt.")

