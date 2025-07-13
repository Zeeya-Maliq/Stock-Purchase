stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3400
}
def calculate_investment():
    total_investment = 0
    print("Enter stock names and their quantities (type 'done' to finish):")
    while True:
        stock_name = input("Stock name (e.g., AAPL, TSLA, etc.): ").upper()
        if stock_name == 'DONE':
            break
        quantity = int(input("Quantity of stocks: "))
        if stock_name in stock_prices:
            investment = stock_prices[stock_name] * quantity
            total_investment += investment
            print(f"You invested in {quantity} shares of {stock_name} for {investment} GBP.")
        else:
            print(f"Stock {stock_name} not found in the database.")
    return total_investment
def save_to_file(total_investment):
    with open("investment_summary.txt", "w") as file:
        file.write(f"Total Investment: {total_investment} GBP")
    print(f"Total investment saved to investment_summary.txt")
if __name__ == "__main__":
    total_investment_value = calculate_investment()
    print(f"Total Investment Value: {total_investment_value} GBP")
    save_choice = input("Do you want to save the result to a file? (yes/no): ").lower()
    if save_choice == 'yes':
        save_to_file(total_investment_value)
