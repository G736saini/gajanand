num = int(input("enter the number:"))
diviser = True
if num<=1:
   print("not prime")
for i in range(2,num):
   if num%i==0:
      diviser = False
      break
if diviser == False:
   print("not prime")
else:
   print("prime") 