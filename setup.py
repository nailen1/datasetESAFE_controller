from setuptools import setup, find_packages

setup(
    name="datasetESAFE_controller",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "xlrd",
        "shining_pebbles>=0.2.61",
    ],
    author="nailen",
    description="A package for managing and processing ESAFE dataset files",
    python_requires=">=3.8",
)
