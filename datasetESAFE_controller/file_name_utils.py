from .esafe_consts import *
from .excel_utils import open_excel_as_df
import os
from pathlib import Path


def get_file_path(file_name):
    return os.path.join(BASE_PATH, file_name)

def get_date_ref_from_df(df):
    date = df['영업일'].unique()[0]
    return date

def get_date_save_from_file_name(file_name):
    date_save = file_name.split('_')[-1].replace('.xls', '')[:10]
    return date_save

def get_file_name_format(file_name, account_code=ACCOUNT_CODE_TOTAL):
    df = open_excel_as_df(os.path.join(BASE_PATH, file_name))
    date_ref = get_date_ref_from_df(df)
    date_save = get_date_save_from_file_name(file_name)
    file_name = f'menu{MENU_CODE_ESAFE_PRICE}-account{account_code}-at{date_ref}-save{date_save}.xls'
    return file_name

def rename_file(old_name, new_name, folder_path=BASE_PATH):
    old_path = Path(os.path.join(folder_path, old_name))
    new_path = Path(os.path.join(folder_path, new_name))

    print(old_path, new_path)
    if not old_path.exists():
        raise FileNotFoundError(f"File not found: {old_path}")

    old_path.rename(new_path)
    print(f"Renamed: {old_path} -> {new_path}")
    return None
