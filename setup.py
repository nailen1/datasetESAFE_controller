from setuptools import setup, find_packages

setup(
    name="datasetESAFE_controller",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0.0",
        "openpyxl>=3.1.0",
        "xlrd>=2.0.0",
    ],
    author="ESAFE Team",
    description="ESAFE 데이터셋 관리를 위한 컨트롤러 모듈",
    python_requires=">=3.8",
)
