print ("PHYSICS FORMULAS")
print("1. Force")
print("2. Speed")
print("3. Acceleration")
print("4. Density")
print("5. Pressure")

choice = input ("Enter your choice (1-5): ")

if choice == "1":
    mass = float(input("Enter your mass: "))
    acc =float(input("Enter your acceleration:"))
    result = mass * acc
    print ("force =*, result")

elif choice == "2":
    mass = float(input("Enter distance: "))
    time = float(input("Enter time: "))
    result = distance / time
    print("speed =", result)

elif choice == "3":
    vf = float(input("Enter final velocity: "))
    vi = float(input("Enter initial velocity: "))
    time = float(input("Enter time: "))
    result = (vf - vi) / time
    print("acceleration =", result)

elif choice == "4":
    mass = float(input("Enter mass: "))
    volume = float(input("Enter volume: "))
    result = force / arear
    print("density =", result)

elif choice == "5":
    mass = float(input("Enter for force: "))
    area = float(input("Enter for area: "))
    result = force / area
    print("pressure =", result)

else:
    print("Invalid choice")



