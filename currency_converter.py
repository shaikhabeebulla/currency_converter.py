def currency_converter(amt, from_currency, to_currency):

    price={
        'USD':1.0,
        'INR':88.60,
        'EUR':0.86,
        'JPY':155.0,
        'GBP':0.75
    }

    if from_currency not in price or to_currency not in price:
        print("Unsupported currency code")
        return None

    # conversion of currency.
    amt_in_usd=amt/price[from_currency] # price[eur]
    converted_amt=amt_in_usd*price[to_currency]

    return converted_amt

print("---------------CURRENCY CONVERTER----------------------")
print("Supported currencies : USD, INR, EUR, JPY, GBP")

amt=float(input("Enter the amount: "))
from_currency=input("From Currency: ").upper()
to_currency=input("To Currency: ").upper()

result=currency_converter(amt, from_currency, to_currency)

if result is not None:
    print(f"{amt:.2f} {from_currency}={result:.2f} {to_currency}")