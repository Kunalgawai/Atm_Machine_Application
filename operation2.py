from operation1 import NewError

def op(a,b):
    if b==0:
        raise NewError
    else:
        return(a/b)