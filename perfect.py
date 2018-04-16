def perfect(m):
  fl=[]
  sum=0
  for i in range(1,m):
    if m%i==0:
      fl=fl+[i]
  for i in range(0,len(fl)):
    sum=fl[i]+sum
  if sum==m:
    return(True)
  else:
    return(False)  

