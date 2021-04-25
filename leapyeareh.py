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
val = 0 
while val ==0:
  try:
    year = input("gib year: ")
    year = int(year)
    #never and I mean never do this. This is horrible, this is the worst code that I have ever written.
    if year < 0:
      year = "no"
      year = int(year)
    val = 1
  except:
    print("you are a moron enter in an actual year")

LeapyearChecker(year)
