
item = input("name:")
price = float(input("unit price:"))
qty = int(input("quantity:"))
# total
total = price * qty
# VAT TAX CHARGE
percentage = 3
vat = price * (percentage/100)
# grand total
grand_total = total + vat
print(f"{item}: total k{total:.2f}")
print(f"vat charge: k{vat}")
print(f"grand total: k{grand_total:.2f}")
