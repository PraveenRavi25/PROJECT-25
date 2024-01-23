def encode(n):
    if len(n)==0:
        return ''
    else:
        return n[0]+str(n.count(n[0]))+encode(n[1:].replace(n[0],""))
n=input("Enter the string:")
str=encode(n)
print(str)
