cost = int(input("enter annual income: "))
tax = float(input("what's product tax in your country(in percentage)? "))
total_tax = cost*tax/100
print("total price (inclusive of tax) is ", total_tax+cost)
