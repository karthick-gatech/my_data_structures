import os

def fillUtil(res, curr, n):
  if curr == 0:
    return True
  for i in range(2*n-curr-1):
    if res[i] == 0 and res[i+curr+1] == 0:
      res[i] = res[i+curr+1] = curr
      if fillUtil(res,curr-1,n):
        return True
      res[i] = res[i+curr+1] = 0
  
  return False

def fill(n):
  res = [0] * (2*n)
  if fillUtil(res, n, n):
    print "Output:{}".format(res)
  else:
    print "Not possible"

fill(70)
