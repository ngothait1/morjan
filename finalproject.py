import time
name=input("what is your name? ")
print("hi "+name+" nice to meet you")
print("this is a special calculator , i would need two numbers from you ")
num1=int(input("first number "))
num2=int(input("second number "))
print("thank you for putting in your numbers ,"+str(num1)+" and "+str(num2)) 
num1_status=""
num2_status=""
if num1%2==0:
    num1_status="even"
else:
    num1_status="odd"
if num2%2==0:
    num2_status="even"
else:
    num2_status="odd"        
print("i can see that the first number is "+num1_status+ "\n" +"And the second number is "+num2_status)
if num1%2==0 and num2%2==0:
    print("so both are even ")
elif num1%2!=0 and num2%2!=0:
    print("so both are odd ")
else:
    print("so one of them is even , and one is odd")
print("operator (+,-,*,/) ",end=" ")
selection=input()
if selection=="*" or selection=="+" or selection=="-" or selection=="/":
   if selection=="/":
     answer=input("you chose division ,should the result be integer? (y/n) ")
   print(str(num1)+" "+selection+" "+str(num2)+" "+"=",end=" ")
   if selection=="*":
     print(num1*num2)
   elif selection=="+":
    print(num1+num2)
   elif selection=="-":
     print(num1-num2)
   elif selection=="/":
      if num2!=0:
       if answer=="y":
         print(num1//num2)
       else:
        print(num1/num2)
else:
   print("error operator" ,selection+" " +"is not supported" +"\n" +"had error occured ,please try again")

print("Thank you" + " " + name +" "+"for using the calculator on "+time.ctime())
