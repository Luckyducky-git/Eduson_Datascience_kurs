import pandas as pd
import numpy as np
import seaborn as sns
from tabulate import tabulate
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
import re
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats
import statsmodels.stats
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# загрузка данных
df_original = pd.read_csv('C:/Users/negoda_dn/Downloads/DataScience-main/DataCollection/heart.csv')

"""Цель кейса №1 по данным о наличие сердечных заболеваний: провести полноценный анализ данных одного из реальных источников данных, используя Python и соответствующие библиотеки для анализа данных."""

#!!! создадим рабочую копию исходного датафрейм для последующего преобразования, чтобы не "трогать" первоначальные данные.
df=df_original

print(df is df_original)
