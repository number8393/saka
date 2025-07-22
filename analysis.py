import yfinance as yf
import datetime
import pandas as pd

symbols = {
    "EUR/USD": "EURUSD=X",
    "GBP/USD": "GBPUSD=X",
    "USD/JPY": "JPY=X",
    "USD/CHF": "CHF=X",
    "AUD/USD": "AUDUSD=X",
    "NZD/USD": "NZDUSD=X",
    "USD/CAD": "CAD=X"
}

def analyze_market():
    messages = []
    for name, symbol in symbols.items():
        try:
            data = yf.download(tickers=symbol, period="1d", interval="5m")
            if data.empty:
                messages.append(f"❌ Ошибка {name}: Нет данных")
                continue

            candle = data.iloc[-1]
            price = candle['Close']
            volume = candle['Volume']
            open_price = candle['Open']
            direction = "🔼 Покупка" if price > open_price else "🔽 Продажа"
            confidence = round(abs(price - open_price) / price * 100, 2)

            msg = (
                f"📈 {name}
"
                f"{direction}
"
                f"Цена: {price:.5f}
"
                f"Объём: {volume:.0f}
"
                f"Уверенность: {confidence}%
"
                f"Время сделки: 3 мин"
            )
            messages.append(msg)
        except Exception as e:
            messages.append(f"❌ Ошибка {name}: {str(e)}")
    return "\n\n".join(messages)