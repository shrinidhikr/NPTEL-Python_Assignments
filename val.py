def valley(l):
  k=0
  x = len(l)-1
  for i in range(0,len(l)):
    if min(l) == l[i]:
      k = i
  if len(l) < 2:
    return(False)
  elif (l[0] > l[1] and l[x] > l[x-1]) :
    if l[k] < l[k-1] and l[k] < l[k+1] :
      return (True) 
    else:
      return (False)
  else: 
    return (False)
