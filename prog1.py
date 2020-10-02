from array import *

arr1=array('i',[5,28,9,8,7])
arr2=array('i',[2,3,4,5,6])
sum=array('i',[])

leng=len(arr1)

for i in range(leng):
    sum.append(arr1[i]+arr2[i])
    
print(sum)
sum_of_array_element = 0
for i in range(leng):
    sum_of_array_element+=sum[i]
    
print("Sum of elements of the sum array: {}".format(sum_of_array_element))
    
