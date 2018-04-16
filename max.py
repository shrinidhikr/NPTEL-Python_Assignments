def secondmax(l):
  (mymax,mysecondmax) = (0,0)
  i=0
  a=[]
  for x in l:
    if x not in a:
      a.append(x)
  for i in range(len(a)):
    if a[i]==max(a):
      mymax=a[i]
  a.remove(mymax)
  i=0
  for i in range(len(a)):
    if a[i]==max(a):
      mysecondmax=a[i]
  return(mysecondmax)

