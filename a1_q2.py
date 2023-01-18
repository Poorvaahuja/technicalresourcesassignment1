M=int(input('Enter marks of student:'))
def Marks(M):
  if M>=90:
    print('Excellent')
  elif M>=80 and M<90:
    print('Good')
  elif M>=70 and M<80:
    print('Fair')
  elif M>=60 and M<70:
    print('Meets expectation')
  else:
    print('Below par')
Marks(M)
