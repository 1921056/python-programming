sub1 = int(input("Enter marks of sub 1 :"))
sub2 = int(input("Enter marks of sub 2 :"))
sub3 = int(input("Enter marks of sub 3 :"))

if (sub1 < 33 and sub2 < 33 and sub3 < 33):
    print("Student is fail can't able to cross the cut off each one of the subject")

elif ((sub1+sub2+sub3)/300*100) < 40:
    print("you are fail baecause student can't able to cut off total marks")

else:
    print("You are pass")
