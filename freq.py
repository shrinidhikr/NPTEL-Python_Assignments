def frequency(l):
  count=0
  a=[]
  b=[]
  c=[]
  minfreqlist=[]
  maxfreqlist=[]
  for x in l:
    count=0
    for i in range(len(l)):
      if x == l[i]: 
        count= count+1
    a.append((count,x))
  for y in a:
    if y not in b:
      b.append(y)
  c = sorted(b)
  
  for i in range(len(c)):
    if c[0][0] == c[i][0]:
      minfreqlist.append(c[i][1])
  for i in range(len(c)):
    if c[-1][0] == c[i][0]:
      maxfreqlist.append(c[i][1])
    
  return((sorted(minfreqlist),sorted(maxfreqlist)))
    
   
