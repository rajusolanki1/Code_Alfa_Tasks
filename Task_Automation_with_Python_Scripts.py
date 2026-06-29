# Task_Automation_with_Python_Scripts.py

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 135
}

total_investment = 0

with open("stock_report.txt", "w") as file:
    file.write("----- Stock Investment Report -----\n\n")

    while True:
        stock = input("Enter stock symbol (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()

        if stock not in stock_prices:
            print("Stock not found!")
            continue

        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}")

        file.write(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}\n")

        choice = input("Do you want to add another stock? (yes/no): ").lower()

        if choice != "yes":
            break

    file.write(f"\nTotal Investment = ${total_investment}")

print("\n----- Investment Summary -----")
print(f"Total Investment Value: ${total_investment}")
print("Report saved as 'stock_report.txt'")
