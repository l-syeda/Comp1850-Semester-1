# Week 1.2, Session 2: Task 6

temperature = int(input("Enter the machine's temperature in Celsius 1 for operating, 0 for stopped):"))
pressure = int(input("Enter machine's pressure:"))
status = int(input("Choose machine's operating status: "))


if temperature>80:
    print("Temperature is too high. Shut down machine.")
elif temperature>=50 and temperature<=80:
    print("Temperature is within safe limits!")
elif temperature<50:
    print("Temperature is low. No action needed.")
else:
    exit()

if pressure>100:
    print("High pressure detected. Maintainence needed.")
elif pressure>=70 and pressure<=100:
    print("Pressure is stable!")
elif pressure<70:
    print("Low pressure. System operating as normal.")
else:
    exit()

    






