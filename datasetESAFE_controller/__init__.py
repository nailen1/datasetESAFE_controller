"""
datasetESAFE_controller package

A package for managing and processing ESAFE dataset files.
"""

__version__ = '0.1.0'
__author__ = 'nailen'

from .excel_utils import open_excel_as_df

__all__ = ['open_excel_as_df']
