#1
for i in range(1, 11):
    print(i)

#2
for i in range(1, 11):
    print(5, "x", i, "=", 5*i)

#3
for i in range(2, 101, 2):
    print(i)


#8
n = int(input("Enter terms: "))
a, b = 0, 1
for i in range(n):
    print(a)  #here a is the first number
    a, b = b, a+b 
#here it says that the first number that we input after that it becomes second number which is b and b will become the addition of pervious number 

    
#6
for i in range(1, 11):
    print(i * i)
#square of any___ = a*a 

#7
for i in range(10, 0, -1):
    print(i)
# here 10= from where to start,  0=till where , -1 = difference 