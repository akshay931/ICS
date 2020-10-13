file1 = open("input",'r')
file2 = open("output",'w')
for line in file1:
    a,b=(int(x) for x in line.split(" "))

def gcd(num1,num2):
    if(num1==0):
        return num2
    return gcd(num2%num1,num1)

file2.write(str(gcd(a,b)))
