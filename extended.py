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
for index,x in enumerate(num1):
    g,a1,b1 = extended(int(num1[index]),int(num2[index]))
    file2.write(str(index)+" GCD("+str(num1[index])+","+str(num2[index])+") = "+str(g)+"\n")
    file2.write(str(index)+" Coefficient of x is "+str(a1)+"\n")
    file2.write(str(index) +" Coefficient of y is "+str(b1)+"\n\n")
