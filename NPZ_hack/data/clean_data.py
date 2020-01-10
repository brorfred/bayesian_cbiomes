
import numpy as np
import pandas as pd
import pylab as pl

def read_chl(fn="Chl_cleaned.xlsx"):
    """Read Chl data"""
    return pd.read_excel(fn, parse_dates=[0,], na_values="nd", index_col="Date")

def read_nutrients(fn="nutrientdata-1.xls"):
    """Read Nutrient data"""
    return pd.read_excel(fn, na_values="nd", index_col="Date")

def read_zoo(fn="m.leidyi_clean.xls"):
    """Read Zooplankton data"""
    return pd.read_excel(fn, index_col="Date")

def load():
    phy = read_chl()["surface chla all"] 
    phy = phy.loc[~phy.index.duplicated(keep='first')]
    zoo = read_zoo()
    zoo = zoo["less1cm_m3"]*.1 + zoo["more1cm_m3"]
    zoo = zoo.loc[~zoo.index.duplicated(keep='first')]
    nut = read_nutrients() 
    nut = nut[nut.Depth=="S"]["DIN"]
    nut = nut.loc[~nut.index.duplicated(keep='first')]
    return pd.DataFrame(dict(phy=phy,zoo=zoo,nut=nut))["2004":"2018"]

    """
    Ctenophore Dry weight 0.6% to 1% of wetweight, average 0.8%
    0.4% nitrogen of drywidht 

    Each indivudual 5gr wet weight, 0.16mg N 0.01muM



    """