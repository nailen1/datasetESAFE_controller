from .esafe_consts import *
from .excel_utils import open_excel_as_df
import os
from pathlib import Path
from typing import Union


def get_file_path(file_name: str) -> str:
    """
    Constructs the full file path by joining the base path with the file name.

    Args:
        file_name (str): Name of the file

    Returns:
        str: Full path to the file
    """
    return os.path.join(BASE_PATH, file_name)

def get_date_ref_from_df(df) -> str:
    """
    Extracts the reference date from the DataFrame by getting the unique value in the '영업일' column.

    Args:
        df (pandas.DataFrame): DataFrame containing ESAFE data

    Returns:
        str: Reference date extracted from the DataFrame
    """
    date = df['영업일'].unique()[0]
    return date

def get_date_save_from_file_name(file_name: str) -> str:
    """
    Extracts the save date from the file name.
    Expected format: BCI_REDM08003V_YYYYMMDDHHMMSS.xls

    Args:
        file_name (str): Name of the file

    Returns:
        str: Save date in YYYYMMDD format
    """
    date_save = file_name.split('_')[-1].replace('.xls', '')[:10]
    return date_save

def get_file_name_format(file_name: str, account_code: str = ACCOUNT_CODE_TOTAL) -> str:
    """
    Generates a standardized file name based on the ESAFE dataset naming convention.
    Format: menu{MENU_CODE}-account{ACCOUNT_CODE}-at{DATE_REF}-save{DATE_SAVE}.xls

    Args:
        file_name (str): Original file name
        account_code (str, optional): Account code to use in the file name. 
            Defaults to ACCOUNT_CODE_TOTAL.

    Returns:
        str: Formatted file name following the ESAFE dataset naming convention
    """
    df = open_excel_as_df(os.path.join(BASE_PATH, file_name))
    date_ref = get_date_ref_from_df(df)
    date_save = get_date_save_from_file_name(file_name)
    file_name = f'menu{MENU_CODE_ESAFE_PRICE}-account{account_code}-at{date_ref}-save{date_save}.xls'
    return file_name

def rename_file(old_name: str, new_name: str, folder_path: Union[str, Path] = BASE_PATH) -> None:
    """
    Renames a file from old name to new name within the specified folder path.

    Args:
        old_name (str): Current name of the file
        new_name (str): New name for the file
        folder_path (Union[str, Path], optional): Path to the folder containing the file. 
            Defaults to BASE_PATH.

    Raises:
        FileNotFoundError: If the source file does not exist

    Returns:
        None
    """
    old_path = Path(os.path.join(folder_path, old_name))
    new_path = Path(os.path.join(folder_path, new_name))

    print(old_path, new_path)
    if not old_path.exists():
        raise FileNotFoundError(f"File not found: {old_path}")

    old_path.rename(new_path)
    print(f"Renamed: {old_path} -> {new_path}")
    return None
