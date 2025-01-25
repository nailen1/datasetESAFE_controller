import pandas as pd
import os
from pathlib import Path

# Excel 파일이 있는 디렉토리 경로
excel_dir = Path('data/dataset-menuESAFE500068')

# 첫 번째 파일만 읽어서 내용 확인
first_file = next(excel_dir.glob('*.xls'))
print(f"Reading file: {first_file}")

try:
    # 먼저 xlrd 엔진으로 시도
    df = pd.read_excel(first_file, engine='xlrd')
except Exception as e:
    print(f"xlrd engine failed: {e}")
    try:
        # xlrd가 실패하면 openpyxl 엔진으로 시도
        df = pd.read_excel(first_file, engine='openpyxl')
    except Exception as e:
        print(f"openpyxl engine failed: {e}")
        raise

# 데이터프레임의 기본 정보 출력
print("\nDataFrame Info:")
print(df.info())

# 처음 몇 행 출력
print("\nFirst few rows:")
print(df.head())
