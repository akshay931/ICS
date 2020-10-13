file1 = open("input",'r')
file2 = open("output",'w')
for line in file1:
    a,b=(int(x) for x in line.split(" "))
def extended(num1,num2):
    if(num1==0):
        return num2,0,1
    gcd,x,y = extended(num2%num1,num1)
    x1 = y-(num2//num1)*x
    y1 = x
    return gcd,x1,y1
def modinverse(a,m):
    g,x,y = extended(a,m)
    if(g!=1):
        print("multiplicative inverse not exist")
    else:
        return x%m
inv = modinverse(a,b)
g,x,y = extended(a,b)
file2.write("GCD("+str(a)+","+str(b)+") = "+str(g)+"\n")
file2.write("Multiplicative inverse of "+str(a)+" modulo "+str(b)+" is "+str(inv))
