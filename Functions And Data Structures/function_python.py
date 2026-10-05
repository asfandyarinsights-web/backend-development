# bill = 175.00

# taxRate = 15

# totalTax=(bill * taxRate) / 100.00

# print(f"Total Tax : {totalTax}")

# Create A function to do that

def calculatTotalTax(bill , TaxRate):
    return round((bill * TaxRate) / 100.00)


def calculateTotalBill(bill):
    totalTax=float(calculatTotalTax(175.00,15))
    return f"bill : {bill} \ntotal tax is : {totalTax} \ntotal bill is {bill-totalTax}"

print(calculateTotalBill(175.00))
