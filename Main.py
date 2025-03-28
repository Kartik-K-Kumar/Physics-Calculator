print("Equations to ask for below:")
print("1. Stress or pressure")
print("2. Strain")
print("3. Young Modulus")
print("4. Weight")
print("5. Charge")
print("Write Exit to exit the system")

while True:
    equationNum = input("What type of Equation would you like to use? ")
    
    if equationNum.lower() == "exit":
        break

    if equationNum == "1":
        # Stress calculator
        Force = float(input("Enter the force in Newtons (N): "))
        Area = float(input("Enter the area in m^2: "))
        Stress = Force / Area
        print(f"The Stress (Pressure) for a force of {Force} N and an area of {Area} m² is {Stress} Pa")

    elif equationNum == "2":
        # Strain calculator
        OriginalLength = float(input("Enter the original length of the material (before extension): ")) 
        NewLength = float(input("Enter the new length after extension: "))
        Strain = (NewLength - OriginalLength) / OriginalLength
        print(f"The Strain is: {Strain}")

    elif equationNum == "3":
        # Young's Modulus calculator
        Force = float(input("What is the force applied (N): "))
        Area = float(input("What is the cross-sectional area (m²): "))
        Stress = Force / Area
        OriginalLength = float(input("Enter the original length of the material (before extension): ")) 
        NewLength = float(input("Enter the new length after extension: "))
        Strain = (NewLength - OriginalLength) / OriginalLength
        YoungMod = Stress / Strain
        print(f"The Stress is: {Stress} Pa")
        print(f"Young's Modulus is: {YoungMod} Pa")
    elif equationNum == "4":
        #Weight calculator
        Mass = float(input("Whats the mass of the object? "))
        Gravity = float(input("Enter the gravity: "))
        Weight = Mass*Gravity
        print(f"The Weight is: {Weight} N")
    elif equationNum == "5":
        #Charge Calculator
        #Q=it
        Current = float(input("Whats the current? "))
        Time = float(input("Whats the time for the current to pass through? "))
        Charge = Current * Time
        print(f"The charge is :{Charge}C")
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 'Exit'.")

print("Thanks for using the Physics Calculator!")
