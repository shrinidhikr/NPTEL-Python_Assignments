def sumsquares(l):
  m=0
  sum=0
  for a in range(0,len(l)):
    for i in range(0,l[m]+1):
      if l[m] == i*i:
        sum=l[m]+sum
    m=m+1
  return(sum)
