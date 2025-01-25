"""
datasetESAFE_controller package
~~~~~~~~~~~~~~~~~~~~~~~

ESAFE 데이터셋 관리를 위한 컨트롤러 모듈
"""

__version__ = '0.1.0'
__author__ = 'nailen'

from .excel_utils import open_excel_as_df

__all__ = ['open_excel_as_df']
