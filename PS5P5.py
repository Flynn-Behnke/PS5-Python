control = str(input("Would you like to run this program? yes or no? "))
totdiscount = 0
while control == "yes":
  price = float(input("Enter price of item "))
  quant = int(input("Enter quantity "))
  extprice = price*quant
  if extprice > 10000.00:
    discount = extprice*0.25
  else:
    discount = extprice*0.1
  print("The extended price is", extprice, "the discount is", discount, "the total is", extprice-discount)
  totdiscount = totdiscount+discount
  control = str(input("Would you like to run the program again? yes or no? "))
print("Total discounts:", totdiscount)
