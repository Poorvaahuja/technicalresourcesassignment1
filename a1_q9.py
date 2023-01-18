n1=int(input('enter num1:'))
n2=int(input('enter num2:'))
divd=n1
div=n2
#GCD
while(divd%div!=0):
  rem=divd%div
  divd=div
  div=rem
gcd=div
#LCM
lcm=int((n1*n2)/gcd)
print('GCD of two numbers is',gcd)
print('LCM of two numbers is',lcm)
