def quicksortbad(l):
  if len(l) < 2:
    return(l)
  else:
    pivot = l[0]
    smaller = [l[j] for j in range(1,len(l)) if l[j] < pivot]
    bigger = [l[j] for j in range(1,len(l)) if l[j] > pivot]
    rearrange = quicksortbad(smaller) + [pivot] + quicksortbad(bigger)
    return(rearrange)
