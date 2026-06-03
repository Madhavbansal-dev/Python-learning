run=True
print("Power, Total Energy and Electricity bill Calculator".center(59,"-"))
while run:
    try:
        a=int(input("\nTell, What you want to calculate---------\n\n1) Power of your component.\t\t\t(Enter 1)\n2) Total Energy / Work done by your component.\t(Enter 2)\n3) Your Electricity bill.\t\t\t(Enter 3)\n\nEnter Choice: "))
        if a==1:
            run1=True
            while run1:
                wyh=int(input("\nAlso Tell, What values you have in your circuit---------\n\n1) Voltage(V) and Current(A).\t\t(Enter 1)\n2) Current(A) and Resistance(Ω).\t(Enter 2)\n3) Voltage(V) and Resistance(Ω).\t(Enter 3)\n\nEnter the number: "))
                if wyh==1:
                    v=float(input("\nEnter the Voltage(V): "))
                    i=float(input("And, Enter the Current(A): "))
                    if v<0 or i<0:
                        print("\nThese values can't be negative")
                        run1=True
                    else:
                        p=round(v*i,2)
                        print(f"\nThe power of your component is {p}W")
                        run1=False
                elif wyh==2:
                    i=float(input("\nEnter the Current(A): "))
                    r=float(input("And, Enter the Resistance(Ω): "))
                    if i<0 or r<0:
                        print("\nThese values can't be negative.")
                        run1=True
                    else:
                        p=round(i**2*r,2)
                        print(f"\nThe power of your component is {p}W")
                        run1=False
                elif wyh==3:
                    v=float(input("\nEnter the Voltage(V): "))
                    r=float(input("And, Enter the Resistance(Ω): "))
                    if v<0 or r<0:
                        print("\nThese values can't be negative.")
                        run1=True
                    else:
                        p=round(v**2/r,2)
                        print(f"\nThe power of your component is {p}W")
                        run1=False
                else:
                    print("\nEnter 1,2, or 3 only.")
            run=False
        elif a==2:
            p=float(input("\nEnter the power of your component(W): "))
            t=float(input("Also, Enter the time your component has worked(s): "))
            if p<0 or t<0:
                print("These values can't be negative.")
            else:
                e=round(p*t,2)
                print(f"\nThe energy consumed by your component is {e}J or {round(e/3600,2)}Wh")
            run=False               
        elif a==3:
            kwh=float(input("\nEnter the total units / kWh consumed by your component or components(kWh): "))
            rate=float(input("Enter the Rate of one Unit / kWh in your place(₹): "))
            if kwh<0 or rate<0:
                print("\nThese values can't be negative.")
            else:
                eb=round(kwh*rate,2)
                print(f"\nThe Electricity bill is ₹{eb}")
            run=False
        else:
            print("\nEnter 1,2, or 3 only.")
    except ValueError:
        print("\nPlease enter valid numeric values.")
    except ZeroDivisionError:
        print("\nPower is undefined because resistance is 0 Ω.")