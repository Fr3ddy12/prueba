
import pandas as pd

def unique_values(df,col):
  return df[col].nunique()
