from ATMExcept import DepositeError, withdrwError,InsuffError
from ATMOperations import Depop,withop,Balenq

from ATMmenu import menu
while (True):
 try:
  menu()
  ch=float(input("Enter a choice: "))
  match(ch):
    case 1:
        try:
            Depop()
        except ValueError:
            print("Dont entrer alnum ,str and symbol as choise")
        except DepositeError :
            print("Dont  enter the negatve number as deosite ")
    case 2:
        try:
            withop()
        except ValueError:
            print("Dont entrer alnum ,str and symbol as choise")
        except withdrwError:
            print("Dont enter the negatve number or zero as deosite ")
        except InsuffError:
            print("Dont have sufficent amount in your account")
    case 3:
        Balenq()
    case 4:
        print("Thanks for using program ")
        break
    case _:
        print("Ur selection wrong operation try again ")
 except ValueError:
      print("Dont entrer alnum ,str and symbol as choise")