def depth(s):
  m=0
  c=0
  for i in range(0,len(s)):
    if s[i] == "(":
      c=c+1
      m=c  
    elif s[i] == ")":
      c=c-1    
  return(m)
