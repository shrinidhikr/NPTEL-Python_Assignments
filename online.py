def maxcount(l):
  count=0
  a=[]
  b=[]
  c=[]
  for x in l:
    count=0
    for i in range(len(l)):
      if x==l[i]:
        count=count+1
    a.append((count,x))
  for y in a:
    if y not in b:
      b.append(y)
  c=sorted(b)
  return(c[-1][0])

a=[]
b=[]
c=[]
d=[]
x=0
while(True):
  line=input("")
  if line=="":
    break
  else:
    a.append(line)

x=int((len(a)/2))
for i in range(x,len(a)):
  b.append(a[i])
for i in range(0,x):
  c.append(a[i])
d=b+c
for i in range(len(d)):
  print(d[i])


def disjointlist(l1,l2):
  for x in l1:
    for y in l2:
      if x==y:
        return(False)
  else:
    return(True)


def squarefree(n):
  for i in range(2,n):
    if n%(i*i)==0:
      return(False)
  else:
    return(True)


def myreverse(l):
  if l==[]:
    return(l)
  else:
    return([l[-1]] + myreverse(l[0:len(l)-1]))

def min3(x,y,z):
  if x <= y:
    if x <= z:
      minimum = x
    else:
      minimum=z
  else:
    if y<=z:
      minimum=y
    else:
      minimum=z
       
