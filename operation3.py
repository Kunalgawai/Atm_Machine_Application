from operation1 import NewError
from operation2 import op

try:
    a=int(input("enter a number"))
    b=int(input("enter b number"))
    c=op(a,b)
except NewError:
    print("Do not enter a 0 in denomenater")

else:
    print("{} / {} ={}".format(a,b,c))