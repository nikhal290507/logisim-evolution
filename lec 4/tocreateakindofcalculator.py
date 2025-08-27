a=float(input("entre a value : "))
calculation=input("entre sign : ")
b=float(input("enter b value : "))
c=a+b
d=a/b
e=a*b
f=a-b
if calculation=="+":
    print("your result is: ",c)
elif (calculation=="-"):
    print("your result is: ",f)
elif (calculation=="*"):
    print("your result is: ",e)
elif (calculation=="/"):
    print("your result is: ",d)
else:
    print("entre a calculation sign: +,/,*&-")
