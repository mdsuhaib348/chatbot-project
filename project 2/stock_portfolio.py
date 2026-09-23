stock_prices = {
     "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}


def calculate_portfolio():

    portfolio = {}
    total_investment = 0

    print("================================")
    print("    STOCK PORTFOLIO TRACKER")
    print("================================")

    print("\nAvailable Stocks:")

    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

    while True:

        symbol = input(
            "\nEnter stock symbol (or 'done' to finish): "
        ).strip().upper()

        if symbol == "DONE":
            break

        if symbol not in stock_prices:
            print("Stock not found!")
            print("Please choose from:", ", ".join(stock_prices.keys()))
            continue

        try:
            quantity = int(
                input(f"Enter quantity of {symbol}: ")
            )

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + quantity

    print("\n================================")
    print("       PORTFOLIO SUMMARY")
    print("================================")

    if not portfolio:
        print("No stocks were added.")
        return

    with open("portfolio_summary.txt", "w", encoding="utf-8") as file:

        file.write("Stock Portfolio Summary\n")
        file.write("=======================\n\n")

        for symbol, quantity in portfolio.items():

            price = stock_prices[symbol]
            value = price * quantity

            total_investment += value

            result = (
                f"{symbol}: {quantity} shares × "
                f"${price} = ${value}\n"
            )

            print(result, end="")
            file.write(result)

        file.write(
            f"\nTotal Investment: ${total_investment}\n"
        )

    print("\nTotal Investment:", f"${total_investment}")
    print("Summary saved to portfolio_summary.txt")


if __name__ == "__main__":
    calculate_portfolio()