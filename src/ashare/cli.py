from __future__ import annotations

import sqlite3
from pathlib import Path

import typer

from ashare.config import load_settings
from ashare.data.storage import DataStore
from ashare.indicators.trend import calculate_moving_average

app = typer.Typer(help="A-share insight CLI")


@app.command()
def init_db() -> None:
    settings = load_settings()
    db_path = Path(settings.get("storage", {}).get("database_url", "sqlite:///data/db/ashare.db")).as_posix().replace("sqlite:///", "")
    conn = sqlite3.connect(db_path)
    conn.execute("CREATE TABLE IF NOT EXISTS sample_market (symbol TEXT, date TEXT, close REAL)")
    conn.commit()
    conn.close()
    typer.echo(f"Database initialized at {db_path}")


@app.command()
def collect(symbols: str = typer.Option("600519,000001", help="Comma separated symbols"),
           start: str = typer.Option("2020-01-01", help="Start date")) -> None:
    symbols_list = [s.strip() for s in symbols.split(",") if s.strip()]
    typer.echo(f"Collecting data for: {symbols_list} from {start}")


@app.command()
def indicators(symbol: str = typer.Option("600519", help="Stock symbol")) -> None:
    values = [10.0, 11.0, 12.0, 13.0, 12.5, 14.0, 15.0]
    result = calculate_moving_average(values, window=3)
    typer.echo(f"{symbol} moving average: {result}")


@app.command()
def report(date: str = typer.Option("today", help="Report date")) -> None:
    typer.echo(f"Generating report for {date}")


if __name__ == "__main__":
    app()
