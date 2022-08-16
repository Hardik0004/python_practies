income = 31234
tax_payable = 0
print("given income", income)
if income < 10000:
    tax_payable = 0
elif income <= 20000:
    x = income-10000
    tax_payable = (x*10)/(100)
else:
    tax_payable = 0
    tax_payable = (1000*10)/(100)
    tax_payable += (income-20000)*(20/100)
    print("total tax to pay is", tax_payable)
