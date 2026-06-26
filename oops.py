l,r,k = (input("enter value of l,r,k").split())

l = int(l)
r = int(r)
k = int(k) 

arr = []
for i in range(l,r+1):
    arr.append(i)
    
temp = len(arr)/k
print("final ans:",temp)