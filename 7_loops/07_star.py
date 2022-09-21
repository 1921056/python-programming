#num=int(input("Enter a number :"))
num=3
#for i in range(1,num,1):
#    print("*" * i)
for i in range (num):
    print(" " * (num-i-1),end="")
    print("*" * (2*i+1),end="")
    print(" " * (num-i-1))
