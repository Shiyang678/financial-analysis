from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd


class DataStore:
    def __init__(self, db_path: str | Path = "data/db/ashare.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

    def save_dataframe(self, df: pd.DataFrame, table_name: str) -> None:
        if df.empty:
            return
        df = df.copy()
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        with pd.option_context("mode.copy_on_write", True):
            df.to_sql(table_name, self.db_path, if_exists="append", index=False)

    def read_dataframe(self, table_name: str, query: str | None = None) -> pd.DataFrame:
        import sqlite3

        conn = sqlite3.connect(self.db_path)
        if query:
            result = pd.read_sql_query(query, conn)
        else:
            result = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        conn.close()
        return result
