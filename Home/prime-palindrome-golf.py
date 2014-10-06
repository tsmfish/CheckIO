__author__ = 'Pavel.Malko'
def golf(n):
 e,r=0,n
 while not e:
  r+=1
  try:
   for i in range(0,len(str(r))//2+1):
    if str(r)[i-1]!=str(r)[-i]:raise
   for i in range(2,r//2):
    if not r%i:raise
   e=1
  except:pass
 return r

print(golf(101))