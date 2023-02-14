x=40
marks=50
grades=100
#if statements
if(x<=20):
    print("Failed")
else:
    print("passed")


#if...elif...else statements
if (marks>=0 and marks<=10):
    print("Failed")
elif marks>10 and marks<=20:
    print("Tried")
elif marks>20 and marks<=30:
    print("Average")
elif marks>30 and marks<=50:
    print("Qualified")


#if...elif...else statements
if grades>=0 and grades<=20:
    print("E")
elif grades>20 and grades<=40:
    print("D")
elif grades>40 and grades<=60:
    print("C")
elif grades>60 and grades<=80:
    print("B")
elif grades>80 and grades<=100:
    print("A")
else:
    print("Y")


