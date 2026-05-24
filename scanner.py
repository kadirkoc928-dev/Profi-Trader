import yfinance as yf
from scoring import swing_score

WATCHLIST = [
    "AAPL","MSFT","NVDA","AMZN","META",
    "TSLA","AMD","GOOGL","NFLX","PLTR",
    "JPM","V","DIS","BA","INTC"
]

def get_data(symbol):
    stock = yf.Ticker(symbol)
    return stock.history(period="3mo")

def scan_market():
    results = []

    for symbol in WATCHLIST:
        try:
            df = get_data(symbol)

            if df is None or len(df) < 20:
                continue

            close = df["Close"]
            volume = df["Volume"]

            rsi = 50  # später upgrade möglich
            ema_trend = close.iloc[-1] > close.mean()
            macd = close.iloc[-1] > close.iloc[-5]
            volume_spike = volume.iloc[-1] > volume.mean() * 1.5
            breakout = close.iloc[-1] > close.max() * 0.98

            score = swing_score(rsi, ema_trend, macd, volume_spike, breakout)

            results.append({
                "symbol": symbol,
                "score": score
            })

        except Exception:
            continue

    return sorted(results, key=lambda x: x["score"], reverse=True)
