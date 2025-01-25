"""
Excel 파일 처리를 위한 유틸리티 함수들
"""

import pandas as pd
from pathlib import Path
from typing import Union


def open_excel_as_df(filepath: Union[str, Path]) -> pd.DataFrame:
    """
    Excel(.xls) 파일을 읽어서 DataFrame으로 반환하는 함수

    Args:
        filepath (Union[str, Path]): 읽을 Excel 파일의 경로

    Returns:
        pd.DataFrame: Excel 파일의 내용을 담은 DataFrame

    Raises:
        FileNotFoundError: 파일이 존재하지 않을 경우
        ValueError: 파일을 DataFrame으로 변환하는데 실패한 경우
    """
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    try:
        # xls 파일은 xlrd 엔진을 사용
        return pd.read_excel(filepath, engine='xlrd')
    except Exception as e:
        raise ValueError(f"Failed to read Excel file: {filepath}") from e
