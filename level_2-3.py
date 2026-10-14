#LEVEL 2:
expenses = []
for i in range(3):
    description = input("Enter Description: ").title().strip()
    category = input("Enter category: ").title().strip()
    amount = float(input("Enter amount spent: "))
    
    exp = {}
    exp["description"] = description
    exp["category"] = category
    exp["amount"] = amount 
    
    expenses.append(exp)

    
print("\n--- All Expenses ---")    
    
for e in expenses:
        print(f"Description: {e['description']}\nCategory: {e['category']}\nAmount: {e['amount']:.2f}")
total = 0
for t in expenses:
    total += t["amount"]
print(f"Total: {total:.2f}") 

category_total = {}
for tot in expenses:
    if tot['category'] not in category_total:
        category_total[tot['category']] = tot['amount']
    else:
        category_total[tot['category']] += tot['amount']
        
print("\n--- Category Summary ---")

for category in category_total:
    print(f"{category}: {category_total[category]:.2f}") 


most_expensive = expenses[0]

for ex in expenses:
    # Compare the current expense with most_expensive
    if ex['amount'] > most_expensive['amount']:
        most_expensive = ex
# Display the most expensive expense   
print(f"Most expensive expense: {most_expensive['category']} {most_expensive['description']} {most_expensive['amount']:.2f}")