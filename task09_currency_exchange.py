#currency exchange

exchange_rate = 150

usd_amount = float(input("Enter amount in USD: "))

etb_amount = usd_amount * exchange_rate

print("=" * 30)
print("EXCHANGE RESULT")
print("-" * 30)
print("USD Amount: $", usd_amount)
print("Exchange Rate: ", exchange_rate)
print("-" * 30)
print("Total ETB: ", etb_amount ,"ETB")
print("=" * 30)