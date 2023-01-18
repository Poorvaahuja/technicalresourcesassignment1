n=int(input('enter number to be rotated:'))
k=int(input('Enter rotating value:'))
a=0
temp=n
while temp>0:
  temp=temp//10
  a=a+1
k=k%a
if k<0:
  k=k+a
div=pow(10,k)
multi=pow(10,(a-k))
rem=n%div
quot=n//div
ans=rem*multi+quot
print(ans)
