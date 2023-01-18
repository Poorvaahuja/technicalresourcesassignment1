n=int(input('Enter the number whose prime factorization is to be displayed:'))
div=2
while(div*div<=n):
  while(n%div==0):
    print(div,end=' ')
    n=n/div
  div+=1
if (n!=1):
  print(int(n))
