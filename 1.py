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

#загрузка данных
df_original = pd.read_csv('C:/Users/negoda_dn/Downloads/DataScience-main/DataCollection/heart.csv')

"""Цель кейса №1 по данным о наличие сердечных заболеваний: провести полноценный анализ данных одного из реальных источников данных, используя Python и соответствующие библиотеки для анализа данных."""

#!!! создадим рабочую копию исходного датафрейм для последующего преобразования, чтобы не "трогать" первоначальные данные.
df=df_original.copy()

#кол-во строк и столбцов таблицы
df.shape

# вычисление корреляций
corr_matrix = df.corr()

# визуализация корреляционной матрицы
fig = px.imshow(corr_matrix)
fig.show()

'''

#зададим наименования столбцов таблицы
cols = df.columns
for i in range(len(cols)):
  print(cols[i])

# Исследуем распределения по данным:
# Рассчитываем кол-во уникальных значений, нулевых и пустых значений + доля в % от общего кол-ва;

# Для каждого столбца выведем: количество уникальных значений, нулевых, NaNs и их долю, а также тип данных в столбцах.

def columnValues(df):
    row = [df.nunique(), (df == 0).sum(axis=0), df.isna().sum(), round(df.isna().sum() / len(df) * 100, 1), df.dtypes]
    return row

data = []
for column in df:
    data.append([column] + columnValues(df[column]))

print(tabulate(data, headers=['название', 'к-во уник знач', 'к-во 0-ых знач', 'пустые','% пустых', 'тип данн'], tablefmt='orgtbl'))

# Age - возраст
# Sex - пол
# ChestPainType - Тип боли в груди [TA: Типичная стенокардия,ATA: Атипичная стенокардия, NAP: Нетипичная
# стенокардия, ASY: Бессимптомная]

# RestingBP - кровяное давление в состоянии покоя [мм рт. ст.]
# Cholesterol - холестерин в сыворотке крови [мм/дл]
# FastingBS - уровень сахара в крови натощак [1: если уровень сахара в крови > 120 мг/дл, 0: в противном случае]
# RestingECG  результаты электрокардиограммы в состоянии покоя [Нормальный: Нормальный, ST: аномалия зубца ST-T (инверсии
# зубца T и/или подъем или понижение ST > 0,05 мВ), ГЛЖ: показывает вероятную или определенную гипертрофию
# левого желудочка по критериям Эстеса]

# MaxHR (Max Heart Rate) - максимальная достигнутая частота сердечных сокращений [Числовое значение от 60 до 202]
# ExerciseAngina - стенокардия, в нагрузке [Y: Да, N: Нет]
# Oldpeak - депрессия ST относится к обнаружению на электрокардиограмме, при котором след в сегменте ST
# аномально низок ниже базовой линии.

# ST_Slope - максимальная нагрузка ST [Вверх: наклон вверх, Плоский: плоский, вниз: наклон вниз
# HeartDisease - наличие сердечных заболеваний [1: сердечные заболевания, 0: норма]

#кол-во строк и столбцов таблицы
df.shape

def columnValues(df):
    row = [df.nunique(), (df == 0).sum(axis=0), df.isna().sum(), round(df.isna().sum() / len(df) * 100, 1), df.dtypes]
    return row

data = []
for column in df:
    data.append([column] + columnValues(df[column]))

print(tabulate(data, headers=['название', 'к-во уник знач', 'к-во 0-ых знач', 'пустые','% пустых', 'тип данн'], tablefmt='orgtbl'))

num_rows = len(df)
num_columns = len(df.columns)
print("Количество строк:", num_rows)
print("Количество столбцов:", num_columns)

# b. Размер DataFrame в оперативной памяти
memory_usage = df.memory_usage().sum()
print("Размер DataFrame в памяти:", memory_usage, "байт")

# c. Анализ интервальных переменных
numerical_columns = df.select_dtypes(include=[int, float]).columns
for column in numerical_columns:
    print("Статистика для столбца", column)
    print ("стандартное отклонение", df[column].std())
    print("Минимальное значение:", df[column].min())
    print("Медиана:", df[column].median())
    print("Среднее значение:", df[column].mean())
    print("Максимальное значение:", df[column].max())
    print("10-й персентиль:", df[column].quantile(0.1))
    print("25-й персентиль:", df[column].quantile(0.25))
    print("75-й персентиль:", df[column].quantile(0.75))
    print("90-й персентиль:", df[column].quantile(0.9))
    print("----------------------------------------------")

# d. Анализ категориальных переменных
categorical_columns = df.select_dtypes(include=[object]).columns
for column in categorical_columns:
    print("Статистика для столбца", column)
    mode = df[column].mode()[0]
    mode_count = df[column].value_counts()[mode]
    unique_values = df[column].nunique()
    print("Мода:", mode)
    print("Количество встреч моды:", mode_count)
    print("Уникальные значения:", unique_values)

# второй метод describe() возвращает сводную статистическую информацию о числовых столбцах в DataFrame,

df.describe()

#  FastingBS показатель уровня сахара в крови (1 знач высокий)
df.groupby('FastingBS').count().head(10)

df.groupby('Age').count().head(10)

# найдем среднее значение
df.groupby('Age')['Age'].mean().head()

df.groupby('Sex').count().head(10)

df.groupby('Cholesterol').count().head(100)

# Посмотрим, сколько экземпляров каждого класса в датасете
import pandas as pd
# метод info()
print(df.info())

# метод columns()
print(df.columns)

# Посмотрим зависимость пола по возрастным категориям, чтобы понять % соотношение М и Ж по возрасту
grouped = df.groupby(['Age', 'Sex']).size()
# Затем преобразуем полученные данные в процентное соотношение:
percentages = grouped.groupby(level=0).apply(lambda x: 100 * x / float(x.sum()))
# Результат можно вывести на экран:
print(percentages)

# Преобразуем таблицу в график
formatted = percentages.unstack() # переформатируем таблицу, чтобы индексом был возраст, а столбцами - пол:
formatted.plot(kind='bar', stacked=True)
plt.xlabel('возраст')
plt.ylabel('Процент')
plt.title('Распределение по полу в разбивке по возрасту')
plt.show()

# Выясним зависимость пола от стенокардии (Exercise Angina), чтобы понять % соотношение у М и Ж
grouped = df.groupby(['Sex', 'ExerciseAngina']).size()
# Затем преоьразуем полученные данные в процентное соотношение:
percentages = grouped.groupby(level=0).apply(lambda x: 100 * x / float(x.sum()))
# Результат можно выводим на экран:
print(percentages)

# Преобразуем таблицу в график
def draw_data(data, xlabel, ylabel, title):
    formatted = data.unstack() # переформатируем таблицу, чтобы индексом был пол, а столбцами - %:
    formatted.plot(kind='bar', stacked=True)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

draw_data(percentages, 'Пол', 'Процент заболевания', 'Распределение по полу болеющих стенокардией')

#Преобразуем таблицу в график
formatted = percentages.unstack() # переформатируем таблицу, чтобы индексом был пол, а столбцами - %:
formatted.plot(kind='bar', stacked=True)
plt.xlabel('Пол')
plt.ylabel('Процент заболевания')
plt.title('Распределение по полу болеющих стенокардией')
plt.show()

# Посмотрим зависимость пола от болезни сердца (HeartDisease), чтобы понять % соотношение у М и Ж
grouped = df.groupby(['Sex', 'HeartDisease']).size()
# Затем преобразуем данные в процентное соотношение:
percentages = grouped.groupby(level=0).apply(lambda x: 100 * x / float(x.sum()))
# Результат выводим на экран:
print(percentages)

#Преобразуем таблицу в график
formatted = percentages.unstack() # переформатируем таблицу, чтобы индексом был возраст, а столбцами - пол:
formatted.plot(kind='bar', stacked=True)
plt.xlabel('Пол')
plt.ylabel('Процент заболевания')
plt.title('Распределение по полу и болезни сердца')
plt.show()

# Посмотрим зависимость возраста от болезни сердца (HeartDisease), чтобы понять % соотношение
grouped = df.groupby(['Age', 'HeartDisease']).size()
# Затем преобразуем данные в процентное соотношение
percentages = grouped.groupby(level=0).apply(lambda x: 100 * x / float(x.sum()))
# Выведем результат на экран
print(percentages)

#Преобразуем таблицу в график
formatted = percentages.unstack() # переформатируем таблицу, чтобы индексом был возраст, а столбцами - %:
formatted.plot(kind='bar', stacked=True)
plt.xlabel('Возраст')
plt.ylabel('Процент заболевания')
plt.title('Распределение по возрасту и болезни сердца')
plt.show()

# Age - возраст
# Sex - пол
# ChestPainType - Тип боли в груди [TA: Типичная стенокардия,ATA: Атипичная стенокардия, NAP: Нетипичная
# стенокардия, ASY: Бессимптомная]
# RestingBP - кровяное давление в состоянии покоя [мм рт. ст.]
# Cholesterol - холестерин в сыворотке крови [мм/дл]
# FastingBS - уровень сахара в крови натощак [1: если уровень сахара в крови > 120 мг/дл, 0: в противном случае]
# RestingECG  результаты электрокардиограммы в состоянии покоя [Нормальный: Нормальный, ST: аномалия зубца ST-T (инверсии
# зубца T и/или подъем или понижение ST > 0,05 мВ), ГЛЖ: показывает вероятную или определенную гипертрофию
# левого желудочка по критериям Эстеса]
# MaxHR (Max Heart Rate) - максимальная достигнутая частота сердечных сокращений [Числовое значение от 60 до 202]
# ExerciseAngina - стенокардия, в нагрузке [Y: Да, N: Нет]
# Oldpeak - депрессия ST относится к обнаружению на электрокардиограмме, при котором след в сегменте ST
# аномально низок ниже базовой линии.
# ST_Slope - максимальная нагрузка ST [Вверх: наклон вверх, Плоский: плоский, вниз: наклон вниз
# HeartDisease - наличие сердечных заболеваний [1: сердечные заболевания, 0: норма]

# распределение болезней сердца (HeartDisease) по ЭКГ,полу, грудной боли, стенокардии, сахара
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15,15))
sns.countplot(x='HeartDisease', hue='RestingECG', data=df, ax=axes[0][0])
sns.countplot(x="HeartDisease", hue="Sex", data=df, ax=axes[0][1])
sns.countplot(x="HeartDisease", hue="ChestPainType", data=df, ax=axes[1][0])
sns.countplot(x="HeartDisease", hue="ExerciseAngina", data=df, ax=axes[1][1])
sns.countplot(x="HeartDisease", hue="FastingBS", data=df, ax=axes[2][0])

sns.histplot(data=df, x='Age', bins=10, hue='Sex')
plt.xlabel('возраст')
plt.ylabel('количество')
plt.title('Распределение пола по возрасту')
plt.show()

# проверим сколько в таблице записей о холестерине
sns.histplot(df['Cholesterol'], bins=10)
plt.xlabel('Холестер')
plt.ylabel('Количество записей')
plt.title('Уровень холестерина')
plt.show()

sns.histplot(data=df, x='Age', bins=10, hue='Sex', stat='probability')
plt.xlabel('Возраст')
plt.ylabel('Вероятность')
plt.title('Распределение по возрасту в разбивке по полу')
plt.show()

# Age - возраст
# Sex - пол
# ChestPainType - Тип боли в груди [TA: Типичная стенокардия,ATA: Атипичная стенокардия, NAP: Нетипичная
# стенокардия, ASY: Бессимптомная]
# RestingBP - кровяное давление в состоянии покоя [мм рт. ст.]
# Cholesterol - холестерин в сыворотке крови [мм/дл]
# FastingBS - уровень сахара в крови натощак [1: если уровень сахара в крови > 120 мг/дл, 0: в противном случае]
# RestingECG  результаты электрокардиограммы в состоянии покоя [Нормальный: Нормальный, ST: аномалия зубца ST-T (инверсии
# зубца T и/или подъем или понижение ST > 0,05 мВ), ГЛЖ: показывает вероятную или определенную гипертрофию
# левого желудочка по критериям Эстеса]
# MaxHR (Max Heart Rate) - максимальная достигнутая частота сердечных сокращений [Числовое значение от 60 до 202]
# ExerciseAngina - стенокардия, в нагрузке [Y: Да, N: Нет]
# Oldpeak - депрессия ST относится к обнаружению на электрокардиограмме, при котором след в сегменте ST
# аномально низок ниже базовой линии.
# ST_Slope - максимальная нагрузка ST [Вверх: наклон вверх, Плоский: плоский, вниз: наклон вниз
# HeartDisease - наличие сердечных заболеваний [1: сердечные заболевания, 0: норма]

# df = pd.DataFrame(data)

# # выбираем только числовые столбцы
# df_numeric = df.select_dtypes(include=['int', 'float'])

# # строим график box plot для числовых столбцов с использованием библиотеки Plotly Express
# # визуализируем на экран на экран с помощью метода show() это распределение данных в числовых столбцах
# fig = px.box(df_numeric)
# fig.show()

df.head()

df.info()

import seaborn as sns
import matplotlib.pyplot as plt

plt.style.context('seaborn');

"""# Как построить корреляционную матрицу"""

import pandas as pd
import plotly.express as px

# вычисление корреляций
corr_matrix = df.corr()

# визуализация корреляционной матрицы
fig = px.imshow(corr_matrix)
fig.show()

# Более светлые оттенки цветов на ячейках матрицы представляют
# собой положительную корреляцию, а более темные оттенки, в свою
# очередь, представляют собой отрицательную корреляцию.
# На данном графике мы видим, что болезни сердца имеют высокую
# отрицательную корреляцию с "Mакс.ЧСС" и отрицательную
# корреляцию с "Холестерином", положительная корреляция с " Пиковым
# низким ST ", "голоданием" и "отдыхом".

# Покажем также распределение сердечных заболеваний среди мужчин и женщин.
fig=px.histogram(df, x="HeartDisease", color="Sex",
    hover_data=df.columns,
    title="Distribution of Heart Diseases",
barmode="group")
fig.show()
fig=px.histogram(df, x="ChestPainType", color="Sex",
    hover_data=df.columns,
    title="Distribution of Heart Diseases",
barmode="group")
fig.show()

# Построем pair plot
sns.pairplot(df)

# Age - возраст
# Sex - пол
# ChestPainType - Тип боли в груди [TA: Типичная стенокардия,ATA: Атипичная стенокардия, NAP: Нетипичная
# стенокардия, ASY: Бессимптомная]
# RestingBP - кровяное давление в состоянии покоя [мм рт. ст.]
# Cholesterol - холестерин в сыворотке крови [мм/дл]
# FastingBS - уровень сахара в крови натощак [1: если уровень сахара в крови > 120 мг/дл, 0: в противном случае]
# RestingECG  результаты электрокардиограммы в состоянии покоя [Нормальный: Нормальный, ST: аномалия зубца ST-T (инверсии
# зубца T и/или подъем или понижение ST > 0,05 мВ), ГЛЖ: показывает вероятную или определенную гипертрофию
# левого желудочка по критериям Эстеса]
# MaxHR (Max Heart Rate) - максимальная достигнутая частота сердечных сокращений [Числовое значение от 60 до 202]
# ExerciseAngina - стенокардия, в нагрузке [Y: Да, N: Нет]
# Oldpeak - депрессия ST относится к обнаружению на электрокардиограмме, при котором след в сегменте ST
# аномально низок ниже базовой линии.
# ST_Slope - максимальная нагрузка ST [Вверх: наклон вверх, Плоский: плоский, вниз: наклон вниз
# HeartDisease - наличие сердечных заболеваний [1: сердечные заболевания, 0: норма]

"""# Как определить распределение атрибутов данных"""

# чтобы проверить линейность переменных, построим график распределения и посмотреть на асимметрию функций.
# Оценка плотности ядра (kde) методом сглаживания данных является весьма
# полезным инструментом для построения графика формы распределения.

#Построем график распределения

sns.histplot(df_original['Sex'], kde=True)
plt.show()
sns.histplot(df_original['Age'], kde=True)
plt.show()
sns.histplot(df_original['ChestPainType'], kde=True)
plt.show()
sns.histplot(df_original['RestingBP'], kde=True)
plt.show()
sns.histplot(df_original['Cholesterol'], kde=True)
plt.show()
sns.histplot(df_original['FastingBS'], kde=True)
plt.show()
sns.histplot(df_original['RestingECG'], kde=True)
plt.show()
sns.histplot(df_original['MaxHR'], kde=True)
plt.show()
sns.histplot(df_original['Oldpeak'], kde=True)
plt.show()
sns.histplot(df_original['ST_Slope'], kde=True)
plt.show()
sns.histplot(df_original['HeartDisease'], kde=True)
plt.show()

fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(15, 15))
#  сделаем  размером 15 на 15 дюймов с сеткой из 4 строк и 3 столбцов, в каждой ячейке которой будет по одному графику.
# Каждый график будет находиться в своей оси axs[i, j], которую можно передать в функцию sns.histplot() с
# помощью параметра ax.
sns.histplot(df_original['Sex'], kde=True, ax=axs[0, 0])
sns.histplot(df_original['Age'], kde=True, ax=axs[0, 1])
sns.histplot(df_original['ChestPainType'], kde=True, ax=axs[0, 2])
sns.histplot(df_original['RestingBP'], kde=True, ax=axs[1, 0])
sns.histplot(df_original['Cholesterol'], kde=True, ax=axs[1, 1])
sns.histplot(df_original['FastingBS'], kde=True, ax=axs[1, 2])
sns.histplot(df_original['RestingECG'], kde=True, ax=axs[2, 0])
sns.histplot(df_original['MaxHR'], kde=True, ax=axs[2, 1])
sns.histplot(df_original['Oldpeak'], kde=True, ax=axs[2, 2])
sns.histplot(df_original['ST_Slope'], kde=True, ax=axs[3, 0])
sns.histplot(df_original['HeartDisease'], kde=True, ax=axs[3, 1])

plt.show()

# создает тепловую карту (heatmap)
fig = plt.figure(figsize = (20, 20))
sns.heatmap(df.corr(), annot=True, cmap = 'YlGnBu');

# корреляция сприрмена (Spearman correlation)
corr = df.corr(method='spearman')
corr.style.background_gradient(cmap='coolwarm').set_precision(2)

"""Цель кейса № 2 по данным о сердечным приступах: провести полноценный анализ данных одного из реальных источников данных с помощью языка Python и библиотек для анализа данных."""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#загрузка данных
data = pd.read_csv('C:/Users/omaka/healthcare-dataset-stroke-data.csv')

data.head()

# Находим количество строк и столбцов
num_rows = data.shape[0]
num_column = data.shape[1]
print(f'Количество строк: {num_rows}, количество столбцов: {num_column}')

# Определим количество уникальных, нулевых + % от общего количества
df = pd.DataFrame(data.loc[:, ['id', 'gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status', 'stroke']].nunique(), columns = ['UNIQUE'])
df['NULL'] = pd.DataFrame(data.loc[:, ['id', 'gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status', 'stroke']].isnull().sum())
df['%NULL'] = pd.DataFrame(data.loc[:, ['id', 'gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status', 'stroke']].isnull().sum()/len(data)*100)
df

# Определим среднее, медиану, стандартное отклонение и т.д. для количественных переменных
data.loc[:,['age','avg_glucose_level','bmi']].describe()

# Определим тип данных для каждого столбца
data.dtypes

# Удалим пустые значения
data.dropna(inplace = True)
print(data.isnull().sum())

# Проверим дублирование
data.duplicated().value_counts()

# Найдем качественные переменные
data.describe(exclude='number')

# Создадим графическую визуализацию данных

# Распределение по полу людей с приступами
new_data=data[data['stroke']==1]

print(new_data['gender'].value_counts())

gender_data=list(new_data['gender'].value_counts())

print(gender_data)


plt.pie(gender_data,labels=['Female','Male'],autopct='%.3f%%',explode = [0,0.1])

plt.show()

# Распределение по флажку "курение"
ax = sns.countplot(x='smoking_status', data=data)
ax.bar_label(ax.containers[0])

# Распределение по возрасту
plt.figure(figsize=(10,5))
sns.histplot(new_data['age'],kde=True,color="black")
plt.title("Возрастное распределение людей, у которых случался приступ")
plt.grid()

# Количественное соотношение людей с приступами и без по полу
ax = sns.countplot(x='gender', hue='stroke', data=data, palette='muted', edgecolor='0.4')
for container in ax.containers:
    ax.bar_label(container)

from scipy import stats

# Проверка гипотез
# нулевая гипотеза: люди более взрослого возраста больше подвержены приступам, чем молодые люди
# альтернативная: возраст не имеет существенного влияния на наличие приступов
significance_level = 0.05
old = data[data['age'] >= 50]
young = data[data['age'] < 50]
tstat, pvalue = stats.ttest_ind(a = old.dropna()['stroke'], b = young.dropna()['stroke'], alternative = 'greater', equal_var = False)
print('T-statistic value is: ', tstat)
print('P-value is: ', pvalue)

# визуальное подтверждение
plt.figure(figsize=(12,7))
new_data = data[data['stroke'] == 1]
ax = sns.histplot(data=new_data, x='age', hue='stroke', multiple='stack')
plt.title('Распределение по возрасту людей с приступами ');'''
print(df is df_original)
