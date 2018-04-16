def cou(l):
  count=0
  a=[]
  b=[]
  for x in l:
    count=0
    for i in range(len(l)):
      if x == l[i]: 
        count= count+1
    a.append((count,x))
  for y in a:
    if y not in b:
      b.append(y)
  return(sorted(b))
