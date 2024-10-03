# Main Program

import currency
cash = 100
print(f"Amount in USD : ${cash}")
print("Equivalent EUR : ",currency.USD_EUR(cash))
print("Equivalent GBP : ",currency.USD_GBP(cash))
print("Equivalent JPY : ",currency.USD_JPY(cash))