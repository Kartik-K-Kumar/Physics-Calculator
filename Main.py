print("Equations to ask for below:")
print("1. Stress or pressure")
print("2.  Strain")
print("3. Young Modulus")
Run = 0
print("Write Exit to exit the system")
equationNum = input("What type of Equation would you like to use? ")
while equationNum != "Exit":
  if equationNum == 1:
    # Stress caculator
    Force = float(input("Enter the force in Newtons (N)" ))
    Area = float(input("Enter the Area in m^2"))
    Stress = Force/Area
    print("The Stress also known as pressure, for when the force is: "+ str(Force) +" and the the Area is: "+ str(Area) + "is " + str(Stress))
    # Strain calculator
  elif equationNum == 2:
    OriginalLenght = float(input("Enter the original length of the material (the length before extending it) ")) 
    NewLength = float(input("Enter the new length after extending the material "))
    Strain = NewLength/OriginalLenght
    print("The Strain is: " + str(Strain))
  elif equationNum == 3:
    #Young Modulus caculator
    Force = float(input("What is the force applied: "))
    Area = float(input("What is the cross sectional area: "))
    Stress = Force/Area
    OriginalLenght = float(input("Enter the original length of the material (the length before extending it) ")) 
    NewLength = float(input("Enter the new length after extending the material "))
    Strain = NewLength/OriginalLenght
    print("The Stress is: " + str(Stress))
    print("Young Modulus")
    YoungMod = Stress/Strain
    print("Young Modulus is: " + str(YoungMod))
    
print("Thanks for using the Physics-Calculator")
  
