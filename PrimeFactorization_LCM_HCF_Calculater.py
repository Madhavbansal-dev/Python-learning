#Importing module:-------------
from functools import reduce
#Some variables:-----------
all_no=[]
pl=[]
nl=[]
hcfans=""
#One custom error:------------
class wrong_input(Exception):
    pass
#Inputing numbers:-----------
run=True
while run:
    try:
        hmn=int(input("How many numbers you want to be factorized and find their LCM and HCF: "))
        if hmn<1:
            raise wrong_input
        if hmn>0:
            run=False
            for no in range(0,hmn):
                no=int(input("\nEnter the number: "))
                all_no.append(no)                
    except ValueError:
        print("\nEnter integer number only\n")
        run=True
        all_no=[]
    except wrong_input:
        print("\nEnter valid Natural Number only\n")
        run=True
#Function for making pairs:----------
def mp(all_no,pl):
    if len(all_no)%2==0:
        for i in range(0,len(all_no),2):
            pl.append([all_no[i],all_no[i+1]])
    else:
        for j in range(len(all_no),1,-2):
            pl.append([all_no[-j],all_no[-j+1]])
        pl.append([all_no[-1]])
    return pl
#Prime Factorization function:----------
def pf(all_no):
    for j in all_no:
        org=j
        factors=""
        if org<-1:
            factors+="-1×"
            j=abs(j)
        i=2
        while j>1:
                while j%i==0:
                    j=int(j/i)
                    factors+=str(i)+"×"
                i+=1
        if org<=1:
            if org>-2:
                print(f"{org} has no prime factorization")
            else:
                print(f"The prime factorization of {org} is {factors[:-1]}")
        else:
            print(f"The prime factorization of {org} is {factors[:-1]}")
#HCF function:----------
def hcf(a,b):
    a=abs(a)
    b=abs(b)
    bn=a if a>=b else b
    run=True
    for i in range(bn,0,-1):
        run=False
        if a%i==0 and b%i==0:
            return i
    if run:
        return 0
#LCM function:-----------
def lcm(a,b):
    a=abs(a)
    b=abs(b)
    if hcf(a,b)==0:
        return 0
    return int((a*b)/hcf(a,b))
#Main:------------
mp(all_no,pl)
while len(pl)!=1:
    nl=[]
    if len(pl[-1])==2:
        for j in pl:
            a,b=j
            nl.append(hcf(a,b))
        if len(pl)>=2:
            pl=[]
            mp(nl,pl)      
    else:
        for j in pl:
            if len(j)==2:
                a,b=j
                nl.append(hcf(a,b))
            else:
                [j]=j
                nl.append(j)
        if len(pl)>=2:
            pl=[]
            mp(nl,pl)
      
if len(pl)==1:
    pl=pl[0]
    if len(pl)==1:
        hcfans+="The HCF of only one number cannot be obtained"
    else:
        a,b=pl
 
#Printing for output:----------
pf(all_no)
if len(all_no)==1:
    print("The LCM of only one number cannot be obtained")
elif reduce(lcm,all_no)==0:
    run=False
    for i in all_no:
        if i>0 or i<0:
            run=True
    if not run:
        print("LCM: undefined")
    else:
        print("LCM:",reduce(lcm,all_no))
else:
    print("LCM:",reduce(lcm,all_no))
if len(hcfans)>0:
    print(hcfans)
elif hcf(a,b)==0:
    print("HCF: undefined")
else:
    print("HCF:",hcf(a,b))
