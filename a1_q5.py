n=int(input('Enter the number whose digits has to be counted '))
def countdigit(n):
  d=0
  while n!=0:
    n//=10
    d+=1
  return d
print('Number of digits in n is',countdigit(n))
