#num=int(input("Enter a number :"))
num=3
#for i in range(1,num,1):
#    print("*" * i)
for i in range (num):
    if(i<=2):
        print("* " * 3)
        print("* " + "  " + "* ")
        print("* " * 3)
        break

print("Done")
   
