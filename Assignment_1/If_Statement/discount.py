#Program
bill_amt = int(input("Enter the bill amount:"))
age = int(input("Enter the age of the customer:"))
if age>50:
    discount = bill_amt*0.05
    total_bill = bill_amt - discount
    print(f"Total bill with discount= {total_bill}")
else:
    print(f"Total bill: {bill_amt}")