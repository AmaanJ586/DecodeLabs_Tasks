def main():
    total = 0.0
    expenses = []
    break_word = "done"

    print("Expense Tracker Application")
    print("Enter your expenses one by one.")
    print("Type 'done' when you are finished.")

    while True:
        input_expense = input("Enter expense amount (type 'done' when finished):").strip()

        if input_expense.lower() == break_word:
            print("Exiting...")
            break

        try:
            expense = float(input_expense)
        except ValueError:
            print("Only enter amount in numbers (e.g. 100, 50). Please try again.")
            continue

        if expense < 0:
            print("Expense amount can't be negative. Please try again.")
            continue

        total += expense
        expenses.append(expense)

        print(f"Added {expense: .2f} and total is {total: .2f}")

    print(" Expense Summary:")

    if not expenses:
        print("No expenses found.")
    else:
        for index, expense in enumerate(expenses, start = 1):
            print(f"{index}. {expense: .2f}")

        average = total / len(expenses)
        highest = max(expenses)
        lowest = min(expenses)

        print(f"Total no. of expenses: {len(expenses)}")
        print(f"Average expense: {average: .2f}")
        print(f"Highest expense: {highest: .2f}")
        print(f"Lowest expense: {lowest: .2f}")
        print(f"Total expense: {total: .2f}")

if __name__ == "__main__":
    main()