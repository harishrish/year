year=int(input("enter year":))
if(year%4==0 and year%100!=0 or year%400==0):
  print("this year is leap year")
else:
  print("this year is not leap year")
