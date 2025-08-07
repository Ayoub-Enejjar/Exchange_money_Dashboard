def exchangeable_value():
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    budget = float(input("Enter the amount of your money you are planning to exchange: "))
    denomination = int(input("Enter the denomination of the bills: "))

    spread = 10
    print("Enter your currency exchange rate: ")
    exchange_rates = {
        "USD": 1.10,
        "EUR": 0.92,
        "GBP": 0.78,
        "JPY": 155.30,
        "MAD": 10.20
    }

    currency = input("Enter the currency you want to exchange to (e.g., USD, EUR, GBP): ").upper()

    if currency not in exchange_rates:
        print("Invalid currency. Please enter a valid currency.")
        return None 

    exchange_rate = exchange_rates[currency]


    spread_decimal = spread / 100
    real_rate = exchange_rate * (1 + spread_decimal)
    exchang_amount = budget / real_rate
    number_of_bills = int(exchang_amount // denomination)
    exchangeable_value = number_of_bills * denomination

    print(f"\nThe maximum value you can get in {currency} is: {exchangeable_value}")
exchangeable_value()