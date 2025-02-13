
def checkprime(num):
    if num<=1:
        return False
    for i in  range (2,int(num*0.5)+1):
        if num%i==0:
            return False
            
    return True
print(checkprime(2))
num=123456
result=[]
for i in str(num):
    result.append(int(i))
print(result)
sum=0
for digit in result:
     if checkprime(digit):
         sum+=digit
print(sum)