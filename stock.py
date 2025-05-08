import yfinance as yf
import pandas as pd

# Tickers: Nvidia
tickers = ['NVDA']
names = {'NVDA': 'Nvidia'}
start_date = '2022-01-01'

df_list = []

for ticker in tickers:
    data = yf.download(ticker, start=start_date)
    data = data.reset_index()  # ✅ Convierte el índice en columna 'Date'
    data['Company'] = names[ticker]
    data['Daily Return'] = data['Close'].pct_change()  # Usar 'Close'
    data['Cumulative Return'] = (1 + data['Daily Return']).cumprod() - 1
    data['Volatility_30d'] = data['Daily Return'].rolling(window=30).std()
    df_list.append(data)

final_df = pd.concat(df_list)

# Aplanar el MultiIndex de las columnas (aunque ya no debería haber MultiIndex)
final_df.columns = [' '.join(col).strip() if isinstance(col, tuple) else col for col in final_df.columns]

# Guardar en archivo Excel
final_df.to_excel('stock_data.xlsx', index=False)

print("✅ Datos guardados en 'stock_data.xlsx'")
