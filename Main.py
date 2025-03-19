print("Equations to ask for below:")
print("1. Stress or pressure")
print("2.  Strain")
print("3. Young Moduls")
print("Write Exit to exit the system")
equationNum = input("What type of Equation would you like to use? ")
while equationNum != "Exit":
  if equationNum == 1:
    Force = float(input("Enter the force in Newtons (N)" ))
    Area = float(input("Enter the Area in m^2"))
    Stress = Force/Area
    print("The Stress also known as pressure, for when the force is: "+ str(Force) +" and the the Area is: "+ str(Area) + "is " + str(Stress))
  else:
    print("Ok")
print("Thanks for using the Physics-Calculator")
  
