#You need input() for all these

x = input("Please input a number (cannot be a decimal): ")
def checkforint(x):
    intcheck = False
    while not intcheck:
        intcheck = True
        try:
            int(x)
        except ValueError:
            x = input("input is not an integer. Please input again: ")
            intcheck = False
            continue
        return int(x)
        # x = float(x)
        # if x != int(x):
        #     x = input("input is float: ")
        #     intcheck = False
        # else:
        #     x = int(x)
x = checkforint(x)


#only strings are not accepted
x = input("Please input a number (can be a decimal): ")
def checkforfloat(x):
    floatcheck = False
    while not floatcheck:
        floatcheck = True
        try:
            float(x)
        except ValueError:
            x = input("input is not a float. Please input again: ")
            floatcheck = False
            continue
        
        return float(x)

x = checkforfloat(x)

#this can be optimized and is kinda pointless because everything can be a string (i think)
x = input("Please input anything: ")
def checkforstr(x):
    strcheck = False
    while not strcheck:
        strcheck = True
        try:
            str(x)
        except ValueError:
            x = input("Input is not a string. Please input again: ")
            strcheck = False
            continue
        x = str(x)
        return str(x)

x = checkforstr(x)

