def sumsquares(l):
  sum=0
  for i in range(0,len(l)):
    sum=(l[i]*l[i])+sum
  return(sum)
