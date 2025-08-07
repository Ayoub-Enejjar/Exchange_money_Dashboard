# 💱 Exchange Money Dashboard

A simple Python-based currency exchange calculator that helps users determine the maximum value they can receive in foreign currency based on their budget, exchange rate, spread, and bill denomination.

## 🚀 Features

- Interactive CLI for user input
- Predefined exchange rates for major currencies (USD, EUR, GBP, JPY, MAD)
- Automatic spread calculation (default: 10%)
- Calculates maximum exchangeable value based on bill denomination

## 📦 How It Works

1. User inputs:
   - Budget amount
   - Desired currency
   - Bill denomination
2. The script:
   - Applies a 10% spread to the exchange rate
   - Calculates the real exchange rate
   - Determines how many bills can be obtained
   - Outputs the maximum exchangeable value

## 🧮 Example

```bash
Enter the amount of your money you are planning to exchange: 1000
Enter the denomination of the bills: 20
Enter the currency you want to exchange to (e.g., USD, EUR, GBP): EUR

The maximum value you can get in EUR is: 880
