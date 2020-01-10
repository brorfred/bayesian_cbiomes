
import numpy as np
import pandas as pd
import pylab as pl

def read_chl(fn="Chl_cleaned.xlsx")
    return pd.read_excel(fn, parse_dates=[0,], na_values="nd")

def read_nutrients(fn="nutrientdata-1.xls"):
    return pd.read_excel(fn, na_values="nd")