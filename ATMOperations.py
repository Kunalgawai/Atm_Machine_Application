from ATMExcept import DepositeError,withdrwError,InsuffError
bal=500.0
def Depop():
    damt=float(input("Enter the amount of damount= "))
    if (damt<=0):
        raise DepositeError
    else:
        global bal
        bal=bal+damt
        print("UR Acount ************123 Credited with INR {}".format(damt))
        print("The amount deposited is ",bal)


def withop():
    withdamt = float(input("Enter the amount of damount= "))
    global bal
    if(withdamt<=0):
        raise withdrwError
    elif(withdamt>bal):
        raise git
    else:

        bal = bal - withdamt
        print("UR Acount ************123 debit with INR {}".format(withdamt))
        print("The amount deposited is ", bal)


def Balenq():
    print("The amount you have in your account is =",bal)