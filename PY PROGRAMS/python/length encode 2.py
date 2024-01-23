def encode(n):
    l=[]
    for i in n:
        if i not in l:
            l.append(i)
    y=""
    l1=[]
    for i in l:
        y=y+i+str(n.count(i))
        l1.append(y)
        y=""
    return l1
        
n=input("Enter the string:")
str=encode(n)
print("".join(str))
