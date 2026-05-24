def swing_score(rsi, ema_trend, macd, volume_spike, breakout):
    score = 0

    if 40 <= rsi <= 65:
        score += 20

    if ema_trend:
        score += 25

    if macd:
        score += 20

    if volume_spike:
        score += 15

    if breakout:
        score += 20

    return min(score, 100)
