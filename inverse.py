file2 = open("output",'w')
num1=[];
num2=[];
with open("input",'r') as file1:
    number = file1.readline()
    for index,line in enumerate(file1):
        line = line.split()
        num1.append(line[0])
        num2.append(line[1])
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
#file2.write("GCD("+str(a)+","+str(b)+") = "+str(g)+"\n")
#file2.write("Multiplicative inverse of "+str(a)+" modulo "+str(b)+" is "+str(inv))
for index,x in enumerate(num1):
    inv = modinverse(int(x),int(num2[index]))
    g,x,y = extended(int(x),int(num2[index]))
    file2.write(str(index)+" GCD("+str(num1[index])+","+str(num2[index])+") = "+str(g)+"\n")
    file2.write(str(index)+" Multiplicative inverse of "+str(num1[index])+" modulo "+str(num2[index])+" is "+str(inv)+"\n\n")
