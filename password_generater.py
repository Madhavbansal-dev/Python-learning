import random
import string

class Wrong_len(Exception):
    pass
class SymbolError(Exception):
    pass
    
def gp(chars,l):
    return "".join(random.choices(chars,k=l))  
    
while True:
    try:
        l=int(input("\nEnter the password length: "))
        if l<=0:
            raise Wrong_len
        m=input("\nEnter y/Y for symbols in password ,else Enter n/N or to quit , Enter q/Q: ").lower()
        if "q" ==m:
                break
        elif "y" ==m:
                 chars=string.ascii_letters+string.digits+string.punctuation
        elif "n"==m:
                   chars=string.ascii_letters+string.digits
        else:
            raise SymbolError                     
        a=gp(chars,l)
        print("\nGenerated Password: ",a)
    except SymbolError:
                print("\nEnter only y/Y,n/N or q/Q")
    except ValueError:
        print("\nLength should be in no.")
    except Wrong_len:
        print("\nLength should be in positive no.")
    except OverflowError:
        print("The password is too large")