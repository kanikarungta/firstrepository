from array import *

arr1=array('i',[5,28,9,8,7])
arr2=array('i',[2,3,4,5,6])
sum=array('i',[])

leng=len(arr1)

for i in range(leng):
    sum.append(arr1[i]+arr2[i])

print(sum)
