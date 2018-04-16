def onehop (l):
  a=[]
  b=[]
  
  for i in range(0,len(l)):
    for j in range(0,len(l)):
      if l[i][1] == l[j][0]:
        a.append((l[i][0],l[j][1]))
  a = [ a[i] for i in range(len(a)) if a[i][0] != a[i][1] ]
  b = set(a)
  return(sorted(b))
