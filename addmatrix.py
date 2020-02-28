r=int(input("enter the number of rows"))
c=int(input("enter the number of cols"))
a=[]
b=[]
c=[]
for i in range(r):
    for j in range(c):
        x=int(input("enter the element"))
        a.append(x)
    b.append(a)
    a=[]
for i in range(r):
    for j in range(c):
        x=int(input("enter the element"))
        a.append(x)
    c.append(a)
    a=[]
for i in range(r):
    for j in range(c):
        print(b[i][j]+c[i][j])
