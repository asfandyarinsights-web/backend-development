billTotal=210

discount_1=10

discount_2=20

# 100 < billTotal < 200 
# (100 < bill_total) and (bill_total < 200)
# chained syntax (100 < bill_total < 200)
# 1. It saves typing (DRY Principle)
# The chained version 100 < bill_total < 200 mimics standard mathematical notation. 

if billTotal>100 and billTotal <200:
    print(F"Bill is Greater Than 100")
    billTotal=billTotal-discount_1
elif billTotal>200:
    print(F"Bill is Greater Than 200")
    billTotal=billTotal-discount_2
else:
    print(f"Bill Is Less Than 100!")

print(F"total Bill : {billTotal}")






#Light is currently off
current = False

if current:
    current = False
    print('Turning light off')

if not current:
    current = True
    print('Turning light on')

current = False

# More Efficient
if current:
    current = False
    print('Turning light off')
else: 
    current = True
    print('Turning light on')


# Let's say you want to give a certain discount to customers if they spend over $100. 
# You will also provide an extra discount if that customer is part of a loyalty program.
# If the customer is not part of the loyalty program and did not spend over a $100,
# a service charge of 5% is applied.

loyalty_customer = False
total_bill = 124

# Calculate Discount Func
def calculateDiscount(bill,discount):
    discount=bill-(float(bill/100))*discount
    return discount

if loyalty_customer and total_bill > 100:
    #give 20% discount
    total_bill =calculateDiscount(total_bill,20)
elif total_bill > 100:
    #give 10% discount
    total_bill = calculateDiscount(total_bill,10)
else:
    #sorry no discount, 5% service charge applied.
    print('Sorry, no discount ...')

print('Total Bill: ', float(total_bill))