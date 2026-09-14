from __future__ import annotations

from typing import Any

import pandas as pd


class AkShareSource:
    def __init__(self, token: str | None = None):
        self.token = token

    def fetch_daily_quotes(self, symbol: str, start_date: str | None = None, end_date: str | None = None) -> pd.DataFrame:
        df = pd.DataFrame(
            {
                "symbol": [symbol],
                "date": [start_date or "2024-01-01"],
                "open": [10.0],
                "high": [11.0],
                "low": [9.5],
                "close": [10.8],
                "volume": [1000],
            }
        )
        return df
