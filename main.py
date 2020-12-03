# Leap Year w/ Nest Loop
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print (f"This year {year} is Leap year")
    else:
      print (f"This year {year} is NOT Leap year")
  else:
    print (f"This year {year} is NOT Leap year")
else:
  print (f"This year {year} is NOT Leap year")


