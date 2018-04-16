def transpose(l):
  value=0
  a=[]  
  k = len(l[0])
  for i in range (0,k):
    b=[]
    for j in range (0,len(l)):
      value = l[j][i]
      b.append(value)
    a.append(b) 
  return(a) 
  
