#python program to check it year is a   leap year or not
year =int(input("Enter the year:"))
if year %4==0and year%100!=0 or year%400==0:
 print(year,"is a leap year")
else:
  print(year,"is not a leap year")