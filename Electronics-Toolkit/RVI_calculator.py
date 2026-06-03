from fractions import Fraction
run=True
print("Total Resistance, Voltage drop and Current Calculator".center(59,"-"))
while run:
    try:
        a=int(input("\nTell, what you want to calculate--------\n\n1) Total Resistance(R) (In series)\t(Enter 1)\n2) Total Resistance(R) (In parallel)\t(Enter 2)\n3) Voltage drop,\n   across each component (In series)\t(Enter 3)\n4) Total Current in circuit,\n   and Current through\n   each branch.\t\t(In parallel)\t(Enter 4)\n\nEnter Choice: "))
        if a==1:
            run1=True
            while run1:
                hmc=int(input("\nHow many components, In your circuit have: "))
                if hmc>0:
                    run1=False
                    tcr=0
                    for i in range(hmc):
                        r=int(input("Enter the Resistance of each component(Ω): "))
                        tcr+=r
                    print(f"\nThe Total Resistance of whole circuit is {tcr}")                
                else:
                    print("\nEnter Valid natural number only")
            run=False
        elif a==2:
            run2=True
            while run2:
                hmc=int(input("\nHow many components, In your circuit have: "))
                if hmc>0:
                    run2=False
                    tcr=0
                    for i in range(hmc):
                        r=float(input("Enter the Resistance of each component(Ω): "))
                        tcr+=1/r
                    tcr=Fraction(tcr).limit_denominator()
                    rfrac=1/tcr
                    print(f"\nThe Total Resistance of whole circuit is {round(float(rfrac),2)}Ω")            
                else:
                    print("\nEnter Valid natural number only")
            run=False
        elif a==3:
            run3=True
            while run3:
                hmc=int(input("\nHow many components, In your circuit have: "))
                if hmc>0:
                    run3=False
                    v=float(input("How much the total voltage have in your circuit(V): "))
                    tcr=0
                    er=[]
                    for j in range(hmc):
                        r=float(input("Enter the Resistance of each component(Ω): "))
                        tcr+=r
                        er.append(r)
                    if tcr==0:
                        print("\nThe Current is undefined because total resistance is 0.")
                    else:
                        i=v/tcr
                        for r in er:
                            vd=round(i*r,2)
                            v=round(v-vd,2)
                            print(f"\nThe Voltage drop across {r}Ω component is {vd}V, so the voltage after it is {v}V")
                else:
                    print("\nEnter Valid natural number only")
            run=False
        elif a==4:
            run4=True
            while run4:
                hmc=int(input("\nHow many components, In your circuit have: "))
                if hmc>0:
                    run4=False
                    v=float(input("How much the total voltage have in your circuit(V): "))
                    er=[]
                    i=0
                    for j in range(hmc):
                        r=float(input("Enter the Resistance of each component(Ω): "))
                        er.append(r)
                    for r in er:
                        ie=round(v/r,2)
                        i+=ie
                        print(f"\nThe Current through {r}Ω component is {ie}A")
                    print(f"\nThe total current in your circuit is {i}A")
                else:
                    print("\nEnter Valid natural number only")
            run=False
        else:
            print("\nEnter 1,2, 3 or 4 only.")
        
    except ValueError:
        print("\nPlease enter valid numeric values.")
    except ZeroDivisionError:
        print("\nCalculation undefined because a resistance is 0 Ω.")
        break