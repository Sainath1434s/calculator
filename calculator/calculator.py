#Simple Calculator using python
print("CALCULATOR")
n1 = float(input("enter first number here"))
n2 = float(input("enter second nmumber here"))

print("1.addition")
print("2.multiplication")
print("3.division")
print("4.substraction")
print("5.mod")

ch=int(input("enter your choice from 1-5"))

if ch==1:
    print(n1+n2)
elif ch==2:
    print(n1*n2)
elif ch==3:
    print(n1/n2)
elif ch==4:
    print(n1-n2)
elif ch==5:
    print(n1%n2)
else:
    print("error")