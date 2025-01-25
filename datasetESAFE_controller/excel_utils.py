"""
Excel file processing utilities
"""

import pandas as pd
import warnings
from pathlib import Path
from typing import Union


def open_excel_as_df(filepath: Union[str, Path]) -> pd.DataFrame:
    """
    Opens an Excel (.xls) file and returns its contents as a DataFrame.

    Args:
        filepath (Union[str, Path]): Path to the Excel file to read

    Returns:
        pd.DataFrame: DataFrame containing the Excel file contents

    Raises:
        FileNotFoundError: If the specified file does not exist
        ValueError: If the file cannot be converted to DataFrame
    """
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    try:
        # Suppress xlrd sector size warning
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            # Use xlrd engine for .xls files
            return pd.read_excel(filepath, engine='xlrd')
    except Exception as e:
        raise ValueError(f"Failed to read Excel file: {filepath}") from e
