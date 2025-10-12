def calculate_due(total_bill, amount_paid):
    due = total_bill - amount_paid
    return due

def display_due(due_amount):
    if due_amount > 0:
        print(f"Customer still owes us")
    elif due_amount < 0:
        print(f"The customer overpaid us")
    else:
        print("The customer has completely paid")

def main():
    total_bill = float(input("Enter the total bill amount: Rs."))
    amount_paid = float(input("Enter the amount paid by the customer: Rs."))
    
    due_amount = calculate_due(total_bill, amount_paid)
    display_due(due_amount)

main()


                 