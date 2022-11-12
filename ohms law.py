# ohm's law calculator

# First user interface menu

print ("What value would you like to solve for?")

print ("1. Voltage")
print ("2. Current")
print ("3. Resistance")
print ("4. Power")

choice = input(">>> ")


#These are calling the functions.


if choice == "1":
    i=float(input("Enter current:"))
    r=float(input("Enter resistance:"))
    print ("Voltage =",(i*r))

elif choice == "2":
    r=float(input("Enter resistance:"))
    v=float(input("Enter voltage:"))
    print ("Current =",(v/r))

elif choice == "3":  
    i=float(input("Enter current:"))
    v=float(input("Enter voltage:"))
    print ("Ressistance =",(v/i))
    
elif choice == "4":
    i=float(input("Enter current:"))
    v=float(input("Enter voltage:"))
    print ("Power =",(i*v))

else:
    print ("Invalid number")   
