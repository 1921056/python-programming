def pattern(name):
    for i in range(3):
        if(i==0):
            print("*"*3)
        elif(i==1):
            print("*"*2 +" ")
        else:
            print("*")
    print("Done " + name)

pattern("kishan")