 #LEVEL 1:
expense = {}
des = input("Enter a description: ").title().strip()
cat = input("Enter category: ").title().strip()
amt = float(input("Enter amount spent: "))
if amt <= 0:
    print("Enter a valid number, no negatives allowed")
else:
    expense["amount"] = amt
    expense["description"] = des
    expense["category"] = cat 
    print(f"Description: {expense['description']}\nCategory: {expense['category']}\nAmount: {expense['amount']:.2f}")