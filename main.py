import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

FILE_NAME = "expenses.csv"

# Create CSV file if not exists
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    df.to_csv(FILE_NAME, index=False)

while True:

    print("\n===== SMART EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Expense Summary")
    print("4. Visualize Expenses")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # ADD EXPENSE
    if choice == '1':

        category = input("Enter Category (Food/Travel/Shopping/etc): ")
        amount = float(input("Enter Amount: "))

        date = datetime.now().strftime("%Y-%m-%d")

        new_data = pd.DataFrame({
            "Date": [date],
            "Category": [category],
            "Amount": [amount]
        })

        new_data.to_csv(FILE_NAME, mode='a', header=False, index=False)

        print("Expense Added Successfully!")

    # VIEW EXPENSES
    elif choice == '2':

        df = pd.read_csv(FILE_NAME)

        print("\n===== ALL EXPENSES =====")
        print(df)

    # SUMMARY
    elif choice == '3':

        df = pd.read_csv(FILE_NAME)

        total = df["Amount"].sum()

        print("\nTotal Expense:", total)

        print("\nCategory Wise Summary:")
        print(df.groupby("Category")["Amount"].sum())

    # VISUALIZATION
    elif choice == '4':

        df = pd.read_csv(FILE_NAME)

        category_sum = df.groupby("Category")["Amount"].sum()

        plt.figure(figsize=(6,6))

        plt.pie(
            category_sum,
            labels=category_sum.index,
            autopct='%1.1f%%'
        )

        plt.title("Expense Distribution")

        plt.show()

    # EXIT
    elif choice == '5':

        print("Exiting Smart Expense Tracker...")
        break

    else:
        print("Invalid Choice")