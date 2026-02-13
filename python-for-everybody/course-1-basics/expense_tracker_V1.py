expenses = []
def add_expenses():
    while True:
        try:
            expense = float(input("Enter your expense: "))
            expenses.append(expense)
            break
        except ValueError:
            print("Invalid input, please try again.")

def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded yet.")
    else:
        for e in expenses:
            print(e)

def total_expenses():
    if len(expenses) == 0:
        print("No expenses recorded yet.")
    else:
        running_total = 0 
        for e in (expenses):
            running_total = e + running_total
        print("Total expenses is",running_total)

def delete_expenses():
    if len(expenses) == 0:
        print("No expenses to delete")
        return
    view_expenses()
    try:
        delete = int(input("Enter the number you want to delete: "))
        index = delete - 1
        if 0 <= index < len(expenses):
            remove = expenses.pop(index)
            print("Removed expense:",remove )
        else:
            print("Invalid number")
    except ValueError:
        print("Please enter valid number")

def main():
    while True:
        print("1. Add expenses")
        print("2. View all expenses")
        print("3. See total expenses")
        print("4. Delete an expense ")
        print("5. Exit")

        choice = (input("Choose an option: "))
        if choice == "1":
            add_expenses()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            delete_expenses()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")
main()