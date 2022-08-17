bill = input("What was the total bill? ") #float or int
persons = input("How many people to split the bill? ") #int
tip = input("What tip percentage? ") #int

bill_w_tip = float(bill) * (int(tip)/100+1)
bill_per_person = round(bill_w_tip/int(persons), 2)

print(f"Total bill with tip is {bill_w_tip}. Each persons pays {bill_per_person} ")