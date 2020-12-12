#Written By Sajid
#Problem: URI1080
counter=int(0)
position=int(0)
max=int(0)
for i in range(1, 101):
    temp=int(input())
    if(temp>max):
        max=temp
        position=i

print(max)
print(position)

