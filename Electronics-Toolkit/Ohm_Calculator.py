run=True
print("         ----------OHM'S LAW CALCULATOR----------")
while run:
    try:
        a=int(input("\nTell, What you want to do------\n\n1) Find Voltage(V)\t(Enter 1)\n2) Find Current(I)\t(Enter 2)\n3) Find Resistance(R)\t(Enter 3)\n\nEnter Choice: "))
        if a==1:
            i=float(input("\nEnter Current (A): "))
            r=float(input("Enter Resistance (Ω): "))
            v=round(i*r,2)
            print(f"\nVoltage = {v} V")
            run=False
        elif a==2:
            v=float(input("\nEnter Voltage (V): "))
            r=float(input("Enter Resistance (Ω): "))
            if r==0:
                print("\nCurrent is undefined.")
            else:
                i=round(v/r,2)
                print(f"\nCurrent = {i} A")
            run=False
        elif a==3:
            v=float(input("\nEnter Voltage (V): "))
            i=float(input("\nEnter Current (A): "))
            if i==0:
                print("\nResistance is undefined.")
            else:
                r=round(v/i,2)
                print(f"\nResistance = {r} Ω")
            run=False
        else:
            print("\nEnter 1,2 or 3 only.")
    except ValueError:
        print("\nPlease enter valid numeric values.")
