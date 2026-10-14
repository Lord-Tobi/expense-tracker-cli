expenses = []
print("\n =====  EXPENSE TRACKER  =====")
while True:
    print("=====  =====")
    print("\nMenu:")
    print("\n1. Add Expense")
    print("\n2. View All Expenses")
    print("\n3. View Summary")
    print("\n4. Quit")
    print("\n=====  ======")
    choice_options = ["1", "2", "3", "4"]
    user_input = input("\nEnter a choice: ").strip()
    #To quit:
    if not user_input:
        print("\nEnter a valid choice")
    elif user_input == "4":
        print("\nGoodbye!!!")
        break
    elif user_input not in choice_options:
        print("\nEnter a valid choice as stated in the menu above.")
    elif user_input in choice_options:
        if user_input == "1":
            print("\nAdding Expense...")
        expense = {}

        description = input("Enter Description: ").capitalize().strip()
        if not description:
            print("Enter a description")
            continue

        category = input("Enter Category: ").title().strip()
        if not category:
            print("Enter a category")
            continue

        while True:
            try:
                amount = float(input("Enter amount spent: "))

                if amount <= 0:
                    print("Invalid amount. Please enter a number greater than zero.")
                    continue
                break
            
            except ValueError:
                print("Please enter a valid number.")

        expense['description'] = description
        expense['category'] = category
        expense['amount'] = amount

        expenses.append(expense)
        print("Expense added successfully!")

        if len(expenses) == 1:
            print(
                f"\nExpense:"
                f"\nDescription: {expense['description']}"
                f"\nCategory: {expense['category']}"
                f"\nAmount: {expense['amount']:.2f}"
            )

        elif user_input == "2":
            print("Viewing all expense...")
            print("----- EXPENSES -----")
            if not expenses:
                print("No expenses recorded yet.")
            else:
                for exp in expenses:
                    print(f"\nDescription: {exp['description']}\nCategory: {exp['category']}\nAmount: {exp['amount']:.2f}")
                print("\nAll expenses displayed.")
        elif user_input == "3":
            print("\nViewing Summary...")
            if not expenses:
                print("No expenses recorded yet.")
            else:
                # Calculate and display the summary here
                total = 0
                for e in expenses:
                    total += e['amount']
                print(f"\nTotal amount spent: {total:.2f}")
            
                print("\n----- CATEGORY SUMMARY -----")
                category_total = {}

                for expense in expenses:
                    if expense['category'] not in category_total:
                        category_total[expense['category']] = expense['amount']
                    else:
                        category_total[expense['category']] += expense['amount']
                for category in category_total:
                    print(f"\n{category}: {category_total[category]:.2f}")
                    
                most_expensive = expenses[0]
                for exp in expenses:
                    if exp['amount'] > most_expensive['amount']:
                        most_expensive = exp
                print(
                        f"\nMost expensive expense: "
                        f"{most_expensive['description']} - "
                        f"{most_expensive['category']} - "
                        f"{most_expensive['amount']:.2f}"
                    )
                print("\nSummary displayed successfully.")


# Requirements
