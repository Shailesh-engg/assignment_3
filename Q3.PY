Str_1=input("Enter the string:- ")
def char(Str_1):
  upper=0
  lower=0
  for i in Str_1:
      if i>='a' and i<='z':
       lower+=1

      if i >='A' and i<='Z':
       upper+=1

  print("LowerCase letter in the String",lower)
  print("UpperCase letter in the String",upper)
char(Str_1)
