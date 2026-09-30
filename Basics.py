#Cricket Over Analyser
'''
import array as arr
n=int(input())
a=arr.array('i',map(int,input().split()))
run=0
h_over=0
l_over=0
a_over=0
m_over=0
bytes_used=n*4
for i in range(n):
    run+=a[i]
    h_over=max(h_over,a[i])
    l_over=min(l_over,a[i])
    if(a[i]==0):
        m_over+=1
a_over=run/n
print(f"{'Total runs':<18}:{run}")
print(f"{'Highest over':<18}:{h_over}")
print(f"{'Lowest over':<18}:{l_over}")
print(f"{'Average over':<18}:{a_over}")
print(f"{'Maiden over':<18}:{m_over}")
print(f"{'Bytes used':<18}:{bytes_used}")
    
'''
#Array Surgery
'''
import array as arr
a=arr.array('i',[10,20,30,40,50])
a.append(60)
print(f"{'After Append':<18}:{a}")
a.insert(1,15)
print(f"{'After insert':<18}:{a}")
a.remove(30)
print(f"{'After remove':<18}:{a}")
a.pop(0)
print(f"{'After pop':<18}:{a}")
a.reverse()
print(f"{'After reverse':<18}:{a}")

'''
#Second highest score
'''

import array as arr
n=int(input())
a=arr.array('i',map(int,input().split()))
maxi=a[0]
for i in range(n):
    if(a[i]>maxi):
        maxi=a[i]
maxi2=-1
f=False
for i in range(n):
    if(a[i]>maxi2 and a[i]!=maxi):
        maxi2=a[i]
        f=True
if(f==True):
    print(f"{'Second largest':<18}={maxi2}")
else:
    print(f"{'Second largest':<18}=No second largest")


'''

#Left Rotate By k
'''

import array as arr
n=int(input())
a=arr.array('i',map(int,input().split()))
k=int(input())
k=k%n
b=arr.array('i')
for i in range(k,n):
    b.append(a[i])
for i in range(k):
    b.append(a[i])
print("Left rotated array:",b)

'''
# Merge two sorted Arrays
'''
import array as arr
n=int(input())
a=arr.array('i',map(int,input().split()))
m=int(input())
b=arr.array('i',map(int,input().split()))
c=arr.array('i')
i=0
j=0
while i<n and j<m:
    if a[i]<b[j]:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
while(i<n):
    c.append(a[i])
    i+=1
while(j<m):
    c.append(b[j])
    j+=1
print("Merge Array:",c)

'''

