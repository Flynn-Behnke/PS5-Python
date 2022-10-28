control = str(input("Would you like to run this program? yes or no "))
count = 0
sumgrosspay = 0
while control == "yes":
  lastname = str(input("Enter last name "))
  hours = float(input("Enter hours worked "))
  rate = float(input("Enter hourly pay rate "))
  if hours > 40:
    othours = hours-40
    otpay = othours*rate*1.5
    grosspay = otpay+40*rate
  else:
    grosspay = hours*rate
  count = count + 1
  sumgrosspay = sumgrosspay + grosspay
  print(lastname, "gross pay:", grosspay)
  print("Employee count:", count)
  control = str(input("Would you like to run this program again? yes or no? "))
print("The total gross pay is", sumgrosspay, "and the employee count is", count)
