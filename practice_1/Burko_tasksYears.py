# encoding=utf-8

year = raw_input("Please, enter the year: \n")
year = int(year)

if year%400==0:
   print "Ok"
elif year%100<>0 and year%4==0:
   print "Ok"
else:
   print "No"