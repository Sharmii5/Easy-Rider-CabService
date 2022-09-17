Cars = [
    [
        "WP-1001",
        "Mr.Walter White",
        "With AC",
        "0764545876"
    ],
    [
        "WP-1002",
        "Mr.Jesse Pinman",
        "Without AC",
        "0715638399"
    ],
    [
        "WP-1003",
        "Mr.Gusse Fringg",
        "With AC",
        "0763214598"
    ],
    [
        "WP-1004",
        "Mr.Saul Goodman",
        "Without AC",
        "0753467545"
    ],
    [
        "WP-1005",
        "Mr.Hank Shrader",
        "Without AC",
        "0729340505"
    ]
]

lorries = [
    [
        "NP-2001",
        "Mr.John Cena",
        "2500kg",
        "0761234567"

    ],
    [
        "NP-2002",
        "Mr.Roman Reigns",
        "3500kg",
        "0764321345"
    ],
    [
        "NP-2003",
        "Mr.Ron Weasley",
        "2500kg",
        "0760987678"
    ],
    [
        "NP-2004",
        "Mr.Sirius Black",
        "3500kg",
        "0767432456"
    ],
    [
        "NP-2005",
        "Mr.Randy Orton",
        "3500kg",
        "0764803218"
    ]
]

ThreeWheelers = [
    [
        "CP-3001",
        "Mr.Dasun Shanaka",
        "0764545345"
    ],
    [
        "CP-3002",
        "Mr.Kusal Mendis",
        "0768787654"
    ],
    [
        "CP-3003",
        "Mr.Rohit Sharma",
        "0760989087"
    ],
    [
        "CP-3004",
        "Mr.Dinesh Chandimal",
        "0763421234"
    ],
    [
        "CP-3005",
        "Mr.Ashen Bandara",
        "0763010193"
    ]
]

Trucks = [
    [
        "NW-4001",
        "Mr.Tony Stark",
        "7 ft",
        "0727894740"
    ],
    [
        "NW-4002",
        "Mr.Steve Rogers",
        "12 ft",
        "0792938498"
    ],
    [
        "NW-4003",
        "Mr.Bruce Banner",
        "12 ft",
        "0716749595"
    ],
    [
        "NW-4004",
        "Mr.Clint Barton",
        "7 ft",
        "0756253839"
    ],
    [
        "NW-4005",
        "Mr.Peter Quill",
        "7 ft",
        "0756209839"
    ]
]
Vans = [
    [
        "SP-5001",
        "Mr.Max Mayfield",
        "With AC",
        "0716784647"
    ],
    [
        "SP-5002",
        "Mr.Billy Hargrove",
        "Without AC",
        "0745892030"
    ],
    [
        "SP-5003",
        "Mr.Steve Harrington",
        "Without AC",
        "0719800095"
    ],
    [
        "SP-5004",
        "Mr.Will Byers",
        "With AC",
        "0768888732"
    ],
    [
        "SP-5005",
        "Mr.Mike Wheeler",
        "With AC",
        "0762223876"
    ]
]
assignedCars = [
    [
        "TM-1006",
        "Mr.Dustin Henderson",
        "With AC",
        "0753401761"
    ]
]
assignedLorries = [
    [
        "NP-2006",
        "Mr.Shawn Mendes",
        "2500kg",
        "0764445343"

    ]
]
assignedThreeWheelers = [
    [
        "CP-3006",
        "Mr.Harry Styles",
        "0767665409"
    ]
]
assignedTrucks = [
    [
        "NW-4006",
        "Mr.Johnny Depp",
        "12 ft",
        "0769876721"
    ]
]
assignedVans = [
    [
        "SP-5006",
        "Mr.Daniel Radcliffe",
        "Without AC",
        "0729876543"
    ]
]
while True:
    print("Welcome to our Easy Rider cab service!")
    print("""
    Enter the number according to the operation you want to perform
    
    - Enter 1 if you want to add a new vehicle to the system.
    - Enter 2 if you want to remove a vehicle from the system.
    - Enter 3 if you want to assign a job(hire).
    - Enter 4 if you want to release from assigned job(hire) after completing.
    - Enter 5 if you want to see available vehicles in each category.
    - Enter 6 if you want to exit the system.
    """)

    action = int(input("Enter a number : "))

#ADD
    if action == 1:
        print("""Enter the number according the vehicle you want to add
        
        - Enter 1 if you want to add a car
        - Enter 2 if you want to add a lorry
        - Enter 3 if you want to add a threewheeler
        - Enter 4 if you want to add a truck
        - Enter 5 if you want to add a van
        """)
        addVehicle = int(input("Enter a number according to the vehicle do you want to add : "))

    #ADD CAR
        if addVehicle == 1:
            print("-- Maximum number of passengers 3 and 4 --")
            for Car in Cars:
                id = Cars.index(Car)
                print("Car ID :", id, "   Car Number :", Car[0], "   Car Driver :", Car[1], "    AC Availability :",
                      Car[2], "     Car Driver's Number :", Car[3])
            carNo = input("Enter the car Number :")
            carDriver = input("Enter the car driver :")
            AC = input("Enter whether with AC or without AC :")
            driverNo = input("Enter the car driver's number :")
            addedList = [carNo, carDriver, AC, driverNo]
            Cars.append(addedList)
            for Car in Cars:
                id = Cars.index(Car)
                print("Car ID :", id, "   Car Number :", Car[0], "   Car Driver :", Car[1], "    AC Availability :",
                      Car[2], "     Car Driver's Number :", Car[3])

    #ADD LORRY
        elif addVehicle == 2:
            for lorry in lorries:
                id = lorries.index(lorry)
                print("Lorry ID :", id, "  Lorry Number :", lorry[0], "  Lorry Driver :", lorry[1], "   Max load :", lorry[2],
                      "   Lorry Driver's Number :", lorry[3])
            lorryNo = input("Enter the lorry Number :")
            lorryDriver = input("Enter the lorry driver :")
            maxLoad = input("Enter whether Max load and size 2500kg OR 3500kg :")
            driverNo = input("Enter the lorry driver's number :")
            addedList = [lorryNo, lorryDriver, maxLoad, driverNo]
            lorries.append(addedList)
            for lorry in lorries:
                id = lorries.index(lorry)
                print("Lorry ID :", id, "  Lorry Number :", lorry[0], "  Lorry Driver :", lorry[1], "   Max load :",
                      lorry[2], "   Lorry Driver's Number :", lorry[3])

    #ADD THREEWHEELER
        elif addVehicle == 3:
            print("-- Maximum number of passengers 3 --")
            for threewheeler in ThreeWheelers:
                id = ThreeWheelers.index(threewheeler)
                print("ThreeWheeler ID :", id, "  ThreeWheeler Number :", threewheeler[0], "  ThreeWheeler Driver :", threewheeler[1],
                      "   ThreeWheeler Driver's Number: ", threewheeler[2])
            threewheelerNo = input("Enter the ThreeWheeler Number:")
            threewheelerDriver = input("Enter the ThreeWheeler driver:")
            driverNo = input("Enter the ThreeWheeler driver's number:")
            addedList = [threewheelerNo, threewheelerDriver, driverNo]
            ThreeWheelers.append(addedList)
            for threewheeler in ThreeWheelers:
                id = ThreeWheelers.index(threewheeler)
                print("ThreeWheeler ID :", id, "  ThreeWheeler Number :", threewheeler[0], "  ThreeWheeler Driver :", threewheeler[1],
                      "   ThreeWheeler Driver's Number: ", threewheeler[2])

    #ADD TRUCKS
        elif addVehicle == 4:
            for Truck in Trucks:
                id = Trucks.index(Truck)
                print("Truck ID :", id, "  Truck Number :", Truck[0], "  Truck Driver :", Truck[1], "   Size :",
                      Truck[2], "   Truck Driver's Number :", Truck[3])
            truckNo = input("Enter the truck Number :")
            truckDriver = input("Enter the truck driver :")
            size = input("Enter the truck size whether 7 ft or 12 ft :")
            driverNo = input("Enter the truck driver's number :")
            addedList = [truckNo, truckDriver, size, driverNo]
            Trucks.append(addedList)
            for Truck in Trucks:
                id = Trucks.index(Truck)
                print("Truck ID :", id, "  Truck Number :", Truck[0], "  Truck Driver :", Truck[1], "   Size :",
                      Truck[2], "   Truck Driver's Number :", Truck[3])

    #ADD VAN
        elif addVehicle == 5:
            print("-- Maximum number of passengers 6 and 8 --")
            for Van in Vans:
                id = Vans.index(Van)
                print("Van ID :", id, "  Van Number :", Van[0], "  Van Driver :", Van[1], "   AC Availability :",
                      Van[2], "   Van Driver's Number :", Van[3])
            vanNo = input("Enter the van Number:")
            vanDriver = input("Enter the van driver:")
            AC = input("Enter whether with AC or without AC:")
            driverNo = input("Enter the van driver's number:")
            addedList = [vanNo, vanDriver, AC, driverNo]
            Vans.append(addedList)
            for Van in Vans:
                id = Vans.index(Van)
                print("Van ID :", id, "  Van Number :", Van[0], "  Van Driver :", Van[1], "   AC Availability :",
                      Van[2], "   Van Driver's Number :", Van[3])

#REMOVE
    elif action == 2:
        print("""Enter the number according the vehicle you want to remove
        
            - Enter 1 if you want to remove a car
            - Enter 2 if you want to remove a lorry
            - Enter 3 if you want to remove a threewheeler
            - Enter 4 if you want to remove a truck
            - Enter 5 if you want to remove a van
            """)
        removeVehicle = int(input("Enter a number : "))

    #REMOVE CAR
        if removeVehicle == 1:
            for Car in Cars:
                id = Cars.index(Car)
                print("Car ID :", id, "   Car Number :", Car[0], "   Car Driver :", Car[1], "    AC Availability :",
                      Car[2], "     Car Driver's Number :", Car[3])
            selectedId = int(input("Enter the car Id which you want to remove : "))
            Cars.pop(selectedId)
            print("-- SUCCESSFULLY REMOVED --")

            for Car in Cars:
                id = Cars.index(Car)
                print("Car ID :", id, "   Car Number :", Car[0], "   Car Driver :", Car[1], "    AC Availability :",
                      Car[2], "     Car Driver's Number :", Car[3])

    #REMOVE LORRY
        elif removeVehicle == 2:
            for lorry in lorries:
                id = lorries.index(lorry)
                print("Lorry ID :", id, "  Lorry Number :", lorry[0], "  Lorry Driver :", lorry[1], "   Max load :",
                      lorry[2], "   Lorry Driver's Number :", lorry[3])
            selectedId = int(input("Enter the lorry Id which you want to remove : "))
            lorries.pop(selectedId)
            print("-- SUCCESSFULLY REMOVED --")

            for lorry in lorries:
                id = lorries.index(lorry)
                print("Lorry ID :", id, "  Lorry Number :", lorry[0], "  Lorry Driver :", lorry[1], "   Max load :",
                      lorry[2], "   Lorry Driver's Number :", lorry[3])

    #REMOVE THREEWHEELER
        elif removeVehicle == 3:
            for threewheeler in ThreeWheelers:
                id = ThreeWheelers.index(threewheeler)
                print("ThreeWheeler ID :", id, "  ThreeWheeler Number :", threewheeler[0], "  ThreeWheeler Driver :",
                      threewheeler[1], "   ThreeWheeler Driver's Number: ", threewheeler[2])
            selectedId = int(input("Select the threewheeler Id which you want to remove : "))
            ThreeWheelers.pop(selectedId)
            print("-- SUCCESSFULLY REMOVED --")

            for threewheeler in ThreeWheelers:
                id = ThreeWheelers.index(threewheeler)
                print("ThreeWheeler ID :", id, "  ThreeWheeler Number :", threewheeler[0], "  ThreeWheeler Driver :",
                      threewheeler[1], "   ThreeWheeler Driver's Number: ", threewheeler[2])

    #REMOVE TRUCKS
        elif removeVehicle == 4:
            for Truck in Trucks:
                id = Trucks.index(Truck)
                print("Truck ID :", id, "  Truck Number :", Truck[0], "  Truck Driver :", Truck[1], "   Size :",
                      Truck[2], "   Truck Driver's Number :", Truck[3])
            selectedId = int(input("Enter the truck Id which you want to remove : "))
            Trucks.pop(selectedId)
            print("-- SUCCESSFULLY REMOVED --")

            for Truck in Trucks:
                id = Trucks.index(Truck)
                print("Truck ID :", id, "  Truck Number :", Truck[0], "  Truck Driver :", Truck[1], "   Size :",
                      Truck[2], "   Truck Driver's Number :", Truck[3])

    #REMOVE VANS
        elif removeVehicle == 5:
            for Van in Vans:
                id = Vans.index(Van)
                print("Van ID :", id, "  Van Number :", Van[0], "  Van Driver :", Van[1], "   AC Availability :",
                      Van[2], "   Van Driver's Number :", Van[3])
            selectedId = int(input("Enter the van Id which you want to remove : "))
            Vans.pop(selectedId)
            print("-- SUCCESSFULLY REMOVED --")

            for Van in Vans:
                id = Vans.index(Van)
                print("Van ID :", id, "  Van Number :", Van[0], "  Van Driver :", Van[1], "   AC Availability :",
                      Van[2], "   Van Driver's Number :", Van[3])

#ASSIGN
    elif action == 3:
        print("""Enter the number according the vehicle you want to assign for the hire
        
                - Enter 1 if you want to assign a car
                - Enter 2 if you want to assign a lorry
                - Enter 3 if you want to assign a threewheeler
                - Enter 4 if you want to assign a truck
                - Enter 5 if you want to assign a van
                """)
        vehicleOption = int(input("Which vehicle do you want to assign for the hire : "))

    #ASSIGN CAR
        if vehicleOption == 1:
            print("""Enter the number according to your preference
            
            - Enter 1 if you want your car to have AC
            - Enter 2 if you don't want your Car to have AC 
            """)
            AC_option = int(input("Enter a number : "))
            if AC_option == 1:
                for car in Cars:
                    if car[2] == "With AC":
                        assigned = car
                        id = Cars.index(car)
                        break
            elif AC_option == 2:
                for car in Cars:
                    if car[2] == "Without AC":
                        assigned = car
                        id = Cars.index(car)
                        break
            assignedCars.append(assigned)
            Cars.pop(id)
            print("-- Available cars --")
            print(assignedCars)

    #ASSIGN LORRY
        if vehicleOption == 2:
            for lorry in lorries:
                assigned = lorry
                id = lorries.index(lorry)
                break
            assignedLorries.append(assigned)
            lorries.pop(id)
            print("-- SUCCESSFULLY ASSIGNED --")
            print(assignedLorries)

    #ASSIGN THREEWHEELER
        if vehicleOption == 3:
            for threewheeler in ThreeWheelers:
                assigned = threewheeler
                id = ThreeWheelers.index(threewheeler)
                break
            assignedThreeWheelers.append(assigned)
            lorries.pop(id)
            print("-- SUCCESSFULLY ASSIGNED --")
            print(assignedThreeWheelers)

    #ASSIGN TRUCKS
        if vehicleOption == 4:
            for truck in Trucks:
                assigned = truck
                id = Trucks.index(truck)
                break
            assignedTrucks.append(assigned)
            Trucks.pop(id)
            print(assignedTrucks)

    #ASSIGN VAN
        if vehicleOption == 5:
                print("""Enter the number according to your preference
                
                 - Enter 1 if you want your van to have AC
                 - Enter 2 if you don't want your van to have AC 
                 """)
                AC_option = int(input("Enter a number : "))
                if AC_option == 1:
                    for van in Vans:
                        if van[2] == "With AC":
                            assigned = van
                            id = Vans.index(van)
                            break
                elif AC_option == 2:
                    for van in Vans:
                        if van[2] == "Without AC":
                            assigned = van
                            id = Vans.index(van)
                            break
                assignedVans.append(assigned)
                Vans.pop(id)
                print("-- SUCCESSFULLY ASSIGNED --")
                print(assignedVans)

#RELEASE
    elif action == 4:
        print("""Enter the number according the vehicle you want to release from the hire
        
                   - Enter 1 if you want to release a car
                   - Enter 2 if you want to release a lorry
                   - Enter 3 if you want to release a threewheeler
                   - Enter 4 if you want to release a truck
                   - Enter 5 if you want to release a van
                   """)
        releaseVehicle = int(input("Enter a number : "))

    #RELEASE CAR
        if releaseVehicle == 1:
            print("Assigned Vehicles : ")
            for Car in assignedCars:
                id = assignedCars.index(Car)
                print("Car ID :", id, "   Car Number :", Car[0], "   Car Driver :", Car[1], "    AC Availability :",
                      Car[2], "     Car Driver's Number :", Car[3])
            releaseId = int(input("Enter the car Id which you want to release : "))
            Cars.append(assignedCars.pop(releaseId))
            print("After releasing")
            for Car in assignedCars:
                id = assignedCars.index(Car)
                print("Car ID :", id, "   Car Number :", Car[0], "   Car Driver :", Car[1], "    AC Availability :",
                      Car[2], "     Car Driver's Number :", Car[3])
            for Car in Cars:
                id = Cars.index(Car)
                print("Car ID :", id, "   Car Number :", Car[0], "   Car Driver :", Car[1], "    AC Availability :",
                      Car[2], "     Car Driver's Number :", Car[3])

    #RELEASE LORRY
        if releaseVehicle == 2:
            print("Assigned Vehicles:")
            for lorry in assignedLorries:
                id = assignedLorries.index(lorry)
                print("Lorry ID :", id, "  Lorry Number :", lorry[0], "  Lorry Driver :", lorry[1], "   Max load :",
                      lorry[2], "   Lorry Driver's Number :", lorry[3])
            releaseId = int(input("Enter the lorry Id which you want to release : "))
            lorries.append(assignedLorries.pop(releaseId))
            print("After releasing")
            for lorry in assignedLorries:
                id = assignedLorries.index(lorry)
                print("Lorry ID :", id, "  Lorry Number :", lorry[0], "  Lorry Driver :", lorry[1], "   Max load :",
                      lorry[2], "   Lorry Driver's Number :", lorry[3])
            for lorry in lorries:
                id = lorries.index(lorry)
                print("Lorry ID :", id, "  Lorry Number :", lorry[0], "  Lorry Driver :", lorry[1], "   Max load :",
                      lorry[2], "   Lorry Driver's Number :", lorry[3])

    #RELEASE THREEWHEELER
        if releaseVehicle == 3:
            print("Assigned Vehicles:")
            for threewheeler in assignedThreeWheelers:
                id = assignedThreeWheelers.index(threewheeler)
                print("ThreeWheeler ID :", id, "  ThreeWheeler Number :", threewheeler[0], "  ThreeWheeler Driver :",
                      threewheeler[1], "   ThreeWheeler Driver's Number: ", threewheeler[2])
            releaseId = int(input("Enter the threewheeler Id which you want to release : "))
            ThreeWheelers.append(assignedThreeWheelers.pop(releaseId))
            print("After releasing")
            for threewheeler in assignedThreeWheelers:
                id = assignedThreeWheelers.index(threewheeler)
                print("ThreeWheeler ID :", id, "  ThreeWheeler Number :", threewheeler[0], "  ThreeWheeler Driver :",
                      threewheeler[1], "   ThreeWheeler Driver's Number: ", threewheeler[2])
            for threewheeler in ThreeWheelers:
                id = ThreeWheelers.index(threewheeler)
                print("ThreeWheeler ID :", id, "  ThreeWheeler Number :", threewheeler[0], "  ThreeWheeler Driver :",
                      threewheeler[1], "   ThreeWheeler Driver's Number: ", threewheeler[2])

    #RELEASE TRUCK
        if releaseVehicle == 4:
            print("Assigned Vehicles:")
            for truck in assignedTrucks:
                id = assignedTrucks.index(truck)
                print("Truck ID :", id, "  Truck Number :", truck[0], "  Truck Driver :", truck[1], "   Size :",
                      truck[2], "   Truck Driver's Number :", truck[3])
            releaseId = int(input("Enter the truck Id which you want to release : "))
            Trucks.append(assignedTrucks.pop(releaseId))
            print("After releasing")
            for truck in assignedTrucks:
                id = assignedTrucks.index(truck)
                print("Truck ID :", id, "  Truck Number :", truck[0], "  Truck Driver :", truck[1], "   Size :",
                      truck[2], "   Truck Driver's Number :", truck[3])
            for truck in Trucks:
                id = Trucks.index(truck)
                print("Truck ID :", id, "  Truck Number :", truck[0], "  Truck Driver :", truck[1], "   Size :",
                      truck[2], "   Truck Driver's Number :", truck[3])

    #RELEASE VAN
        if releaseVehicle == 5:
            print("Assigned Vehicles : ")
            for van in assignedVans:
                id = assignedVans.index(van)
                print("Van ID :", id, "  Van Number :", van[0], "  Van Driver :", van[1], "   AC Availability :",
                      van[2], "   Van Driver's Number :", van[3])
            releaseId = int(input("Enter the van Id which you want to release : "))
            Vans.append(assignedVans.pop(releaseId))
            print("After releasing")
            for van in assignedVans:
                id = assignedVans.index(van)
                print("Van ID :", id, "  Van Number :", van[0], "  Van Driver :", van[1], "   AC Availability :",
                      van[2], "   Van Driver's Number :", van[3])
            for van in Vans:
                id = Vans.index(van)
                print("Van ID :", id, "  Van Number :", van[0], "  Van Driver :", van[1], "   AC Availability :",
                      van[2], "   Van Driver's Number :", van[3])

#VIEW
    elif action == 5:
        print("""Enter the number according the details of the vehicle you want to view
        
                        - Enter 1 if you want to view available cars  
                        - Enter 2 if you want to view available lorries
                        - Enter 3 if you want to view available threewheelers
                        - Enter 4 if you want to view available trucks
                        - Enter 5 if you want to view available vans
                        """)
        viewDetails = int(input("Enter a number : "))
        if viewDetails == 1:
            for Car in Cars:
                id = Cars.index(Car)
                print("Car ID :", id, "   Car Number :", Car[0], "   Car Driver :", Car[1], "    AC Availability :",
                      Car[2], "     Car Driver's Number :", Car[3])
        if viewDetails == 2:
            for lorry in lorries:
                id = lorries.index(lorry)
                print("Lorry ID :", id, "  Lorry Number :", lorry[0], "  Lorry Driver :", lorry[1], "   Max load :",
                      lorry[2], "   Lorry Driver's Number :", lorry[3])
        if viewDetails == 3:
            for threewheeler in ThreeWheelers:
                ThreeWheelers.index(threewheeler)
                print("ThreeWheeler ID :", id, "  ThreeWheeler Number :", threewheeler[0], "  ThreeWheeler Driver :",
                      threewheeler[1], "   ThreeWheeler Driver's Number: ", threewheeler[2])
        if viewDetails == 4:
            for truck in Trucks:
                id = Trucks.index(truck)
                print("Truck ID :", id, "  Truck Number :", truck[0], "  Truck Driver :", truck[1], "   Size :",
                      truck[2], "   Truck Driver's Number :", truck[3])
        if viewDetails == 5:
            for van in Vans:
                id = Vans.index(van)
                print("Van ID :", id, "  Van Number :", van[0], "  Van Driver :", van[1], "   AC Availability :",
                      van[2], "   Van Driver's Number :", van[3])

#END
    elif action == 6:
        break
        