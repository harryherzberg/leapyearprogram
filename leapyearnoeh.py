def LeapyearChecker(year):

  if year%4 == 0: 
    if year%400 == 0:
      print(str(year) + " is leap year")
      return
    if year%100 == 0:
      print(str(year) +" is not leap year")
      return
    print(str(year) +" is leap year")
    return
  print(str(year) +" is not leap year")
year = input("gib year: ")
year = int(year)
LeapyearChecker(year)
