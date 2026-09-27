from pathlib import Path
import pandas as pd


def load_portfolio(file_path: str | Path) -> pd.DataFrame:
    """
    Load a portfolio CSV file into a pandas DataFrame.

    Parameters
    ----------
    file_path : str or Path
        Path to the portfolio CSV file.

    Returns
    -------
    pd.DataFrame
        Portfolio data.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Portfolio file not found: {file_path}")

    if file_path.suffix.lower() != ".csv":
        raise ValueError("Portfolio file must be a CSV file.")

    try:
        portfolio = pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Unable to read portfolio CSV: {e}")

    if portfolio.empty:
        raise ValueError("Portfolio CSV is empty.")

    return portfolio