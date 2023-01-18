low=int(input('Enter the lower limit of the range:'))
high=int(input('Enter the higher limit of the range:'))
print('prime numbers between',low,'&',high)
for i in range(low,high+1):
  num=0
  for j in range(2,i):
    if (i%j==0):
      num=1
      break
  if(num==0):
    print(i,end=' ')
