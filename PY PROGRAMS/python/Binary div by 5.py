n=int(input("Enter the range:"))
l=[]
for i in range(n):
    x=input("Enter the binary values:")
    l.append(x)
l1=[]
for i in l:
    y=int(i,2)
    l1.append(y)
l2=[]
for i in range(len(l1)):
    if(l1[i]%5==0):
        l2.append(l[i])
if(l2==[]):
    print("Not divisible by 5")
else:
    print("Binary numbers only divisible by 5 is",','.join(l2))
