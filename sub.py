def sublist(l1,l2):
  if len(l1) < len(l2):
    for i in range(0, len(l1)):
      for j in range(0, len(l2)):
        if l1[i]==l2[j] and j==i+1:
          pass
      return True
  else:
    return False
