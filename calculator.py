#Addition
def sum(a,b):
    return a+b
#Subtraction
def sub(a,b):
    return a-b
#Multiplication
def mul(a,b):
    return a*b
#Division
def div(a,b):
    return a/b
#distance
def dis(time,s):
    return time*s

#speed
def speed(time,d):
    return d/time
#Simple interest
def simple_interest(p,t,r):
    si=(p*t*r)/100
    return si
#Compound intrest
def compound_interest(p,r,t):
    ci=p*(pow((1+r/100),t))
    return ci
print("select operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiply")
print("4.Divide")
print("5.Distance")
print("6.Speed")
print("7.Simple Intrest ")
print("8.Compound intrest")
while True:
    choice=input("Enter choice(1/2/3/4/5/6/7/8/):")
    if choice in("1","2","3","4"):
        a=float(input("a = "))
        b=float(input("b = "))
        if choice == "1":
            print(a,"+",b,"=",sum(a,b))
        elif choice == "2":
            print(a,"-",b,"=",sub(a,b))
        elif choice == "3":
            print(a,"*",b,"=",mul(a,b))
        elif choice == "4":
            print(a,"/",b,"=",div(a,b))
    elif choice in("5"):
        time=float(input("Enter time(hr) :"))
        s=float(input("Enter speed(km/hr) :"))
        print("Distance is :",dis(time,s),"km")
    elif choice in("6"):
        time=float(input("Enter time(hr) :"))
        d=float(input("Enter Distance(km) :"))
        print("Speed is :",speed(time,d),"km/hr")
    elif choice in("7"):
        p=float(input("Enter Principal :"))
        t=float(input("Enter Time :"))
        r=float(input("Enter Rate :"))
        print("Simple Intrest",simple_interest(p,t,r))
    elif choice in("8"):
        p = float(input("Enter Principal :"))
        t = float(input("Enter Time :"))
        r = float(input("Enter Rate :"))
        print("Compound Intrest",compound_interest(p,r,t))
    else :
        print("Invalid")




