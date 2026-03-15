import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('stocks.csv')

#Apple
print(f"AAPL - Max: {df['AAPL'].max()}")
print(f"AAPL - Min: {df['AAPL'].min()}")
print(f"AAPL - Avg: {df['AAPL'].mean():.2f}")
print()

#Googl
print(f"GOOGL - Max: {df['GOOGL'].max()}")
print(f"GOOGL - Min: {df['GOOGL'].min()}")
print(f"GOOGL - Avg: {df['GOOGL'].mean():.2f}")
print()

#Msft
print(f"MSFT - Max: {df['MSFT'].max()}")
print(f"MSFT - Min: {df['MSFT'].min()}")
print(f"MSFT - Avg: {df['MSFT'].mean():.2f}")
print()

#Plotting Apple stock price
plt.plot(df['Date'], df['AAPL'], label='AAPL')
plt.title('Apple Stock Price')
plt.xlabel('Data')
plt.ylabel('Price')

plt.legend()
plt.gcf().autofmt_xdate()
plt.savefig('plot_apple.png')
plt.clf()

#Plotting Google stock price
plt.plot(df['Date'], df['GOOGL'], label='GOOGL')
plt.title('Goggle Stock Price')
plt.xlabel('Data')
plt.ylabel('Price')
plt.legend()
plt.gcf().autofmt_xdate()
plt.savefig('plot_google.png')
plt.clf()

#Plotting Microsoft stock price
plt.plot(df['Date'], df['MSFT'], label='MSFT')
plt.title('Microsoft Stock Price')
plt.xlabel('Data')
plt.ylabel('Price')
plt.legend()
plt.gcf().autofmt_xdate()
plt.savefig('plot_microsoft.png')
plt.clf()

#Plotting all Stocks Together
plt.plot(df['Date'], df['AAPL'], label='AAPL')
plt.plot(df['Date'], df['GOOGL'], label='GOOGL')
plt.plot(df['Date'], df['MSFT'], label='MSFT')
plt.title('Stock Prices Comparison')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.gcf().autofmt_xdate()
plt.savefig('plot_comparison.png')
plt.clf()