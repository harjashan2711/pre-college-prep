while True :
    try :
        x = float(input("enter first number :"))
        y = input("enter sign :")
        z = float(input("enter second number :"))
        break
    except ValueError :
        print("please enter a number")
        if y == "+"  :
            print(x + z)
        elif y == "-" :
            print(x - z)
        elif y == "*" :
            print(x * z)
        elif y == "/" and z == 0 :
            print("error")
        elif y == "/" :
            print(x / z)

