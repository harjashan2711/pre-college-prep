while True:    
    try :
        x = int(input("what is x? "))
        
        break
    except ValueError :
        print("x is not a number")
print("x is",x)