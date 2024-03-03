# ROI calculator script
# Takes in an instruments variables and
# provides a ROI and Profit/Loss for the invested amount on execution

# User input
cryptocurrecy = input("Cryptocurrency: ")
current_price = float(input("Current price: "))
target_price = float(input("Target price: "))
investment_amount = float(input("Investment amount: "))

# ROI calculator
percentage_change = ((target_price - current_price) / current_price) * 100
coins_tokens_available = investment_amount / current_price

unrealized_bal = target_price * coins_tokens_available
roi = ((unrealized_bal - investment_amount) / investment_amount) * 100

profit = (roi * investment_amount) / 100

# Prints
print("\n-----CURRENCY--COMMODITY--BAL--ROI--P/L-----")
print(f"Cryptocurrecy: {cryptocurrecy}")
print(f"Price change in %: O{current_price} C{target_price} ({percentage_change:.2f}%)")
print(f"{cryptocurrecy} balance: {coins_tokens_available:.8f}")
print(f"Investment Amount: ${investment_amount:.2f}")
print("----------------------------------------------")
print(f"Unrealized Balance: {unrealized_bal:.2f}")
print(f"ROI: {roi:.2f}%")
print(f"P/L: ${profit:.2f}")
print("----------------------------------------------")
print("--Risk disclosure: Not financial advice--")
