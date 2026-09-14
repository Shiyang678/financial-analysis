from __future__ import annotations


def market_summary(prices: list[float]) -> dict:
    if not prices:
        return {"count": 0, "avg": 0.0, "max": 0.0, "min": 0.0}
    return {
        "count": len(prices),
        "avg": round(sum(prices) / len(prices), 4),
        "max": max(prices),
        "min": min(prices),
    }
