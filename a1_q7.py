n=int(input('Enter the number to be inverted:'))
op=1
inv=0
while n>0:
  od=n%10
  np=od
  nd=op
  multi=pow(10,np-1)
  inv=inv+nd*multi
  op=op+1
  n//=10
print(inv)
