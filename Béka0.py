import pyomo.environ as pyo
import pandas as pd
import glob

import csv
import matplotlib.pyplot as plt
import math
import random
from pyomo.opt import SolverFactory
from pyomo.core import Var
import pyomo.environ as en
import seaborn as sns
import time

# HUPX adatok


files = glob.glob("HUPX_DAM_Price_Volume_*.xlsx")

all_data = []

for file in files:
    df = pd.read_excel(file)

    df.columns = df.columns.str.strip()

    df_all = df.melt(
        id_vars=["Delivery Day"],
        value_vars=[col for col in df.columns if "H" in col],
        var_name="Hour",
        value_name="Price"
    )
    df_all["Hour"] = (
        df_all["Hour"]
        .str.extract(r"H(\d+)")[0]
        .astype(int))

    all_data.append(df_all)

# Összefűz
df_all = pd.concat(all_data)

# Időrendbe rendez
df_all = df_all.sort_values(
    by=["Delivery Day", "Hour"]
).reset_index(drop=True)

# Ár tömb
prices = df_all["Price"].to_numpy()




