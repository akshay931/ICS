file2 = open("output",'w')
num1=[];
num2=[];
with open("input",'r') as file1:
    number = file1.readline()
    for index,line in enumerate(file1):
        line = line.split()
        num1.append(line[0])
        num2.append(line[1])

def gcd(num1,num2):
    if(num1==0):
        return num2
    return gcd(num2%num1,num1)
for index,x in enumerate(num1):
    gcd1 = gcd(int(num1[index]),int(num2[index]))
    file2.write("GCD("+str(num1[index])+","+str(num2[index])+") ="+str(gcd1)+"\n\n")
