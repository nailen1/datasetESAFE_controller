"""
excel_handler
~~~~~~~~~~~~

Excel 파일 처리를 위한 핸들러 모듈
"""

import pandas as pd
from pathlib import Path
from typing import Union, List


class ExcelHandler:
    def __init__(self, data_dir: Union[str, Path]):
        """
        Excel 파일 처리를 위한 핸들러 초기화

        Args:
            data_dir: Excel 파일이 있는 디렉토리 경로
        """
        self.data_dir = Path(data_dir)
        if not self.data_dir.exists():
            raise FileNotFoundError(f"Directory not found: {self.data_dir}")

    def read_excel_file(self, file_path: Union[str, Path]) -> pd.DataFrame:
        """
        Excel 파일을 읽어서 DataFrame으로 반환

        Args:
            file_path: 읽을 Excel 파일 경로

        Returns:
            pd.DataFrame: 읽어들인 데이터
        """
        try:
            return pd.read_excel(file_path, engine='xlrd')
        except Exception as e:
            try:
                return pd.read_excel(file_path, engine='openpyxl')
            except Exception as e:
                raise ValueError(f"Failed to read Excel file: {file_path}") from e

    def get_excel_files(self) -> List[Path]:
        """
        디렉토리 내의 모든 Excel 파일 경로 반환

        Returns:
            List[Path]: Excel 파일 경로 리스트
        """
        return list(self.data_dir.glob('*.xls'))
