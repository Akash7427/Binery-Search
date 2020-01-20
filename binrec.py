import time
import random
def binrec(a,f,l,x):
    mid=(f+l)//2
    if x in a:
        if a[mid]==x:
            return mid
        elif x<a[mid]:
            return binrec(a,f,mid-1,x)
        else:
            return binrec(a,mid+1,l,x)
    else:
        return -1

l=list()
a=int(input("Enter no of element:"))
for i in range(0,a):
    
    b=random.randint(0,a)
    print(b)
    l.append(b)
l.sort()
b=int(input("Enter element to be search: "))
f=0
start=time.time()
c=binrec(l,f,a,b)
end=time.time()
diff=end-start
print("The time is:   ",diff)
if c!=-1:
    print("The element is present at:",c+1)
if c==-1:
    print("The element is not present")
