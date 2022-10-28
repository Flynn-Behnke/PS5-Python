control = str(input("Do you want to run this program? yes or no: "))
count = 0
while control == "yes":
  lstname = str(input("Enter last name "))
  score1 = float(input("Enter exam 1 score "))
  score2 = float(input("Enter exam 2 score "))
  avg = (score1 + score2)/2
  print(lstname, "exam average:", avg)
  count = count + 1
  print(count, "people have checked their score")
  control = str(input("Would you like to run this again? Yes or no: "))
print("Have a good day :)")
