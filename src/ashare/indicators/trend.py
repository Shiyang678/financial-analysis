from __future__ import annotations

import pandas as pd


def calculate_moving_average(values: list[float] | pd.Series, window: int = 3) -> list[float]:
    if not values:
        return []

    series = pd.Series(values)
    ma = series.rolling(window=window, min_periods=1).mean()
    return ma.round(4).tolist()
