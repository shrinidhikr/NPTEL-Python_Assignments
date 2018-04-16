def ascending(l):
  for i in range (1,len(l)):
    if l[i] < l[i-1]:
      return(False)
  else: 
    return(True)
