# Выбрать тест и проверить, есть  ли различия между выборками:

# 1 )  Даны две  независимые выборки. Не соблюдается условие нормальности

# x1  380,420, 290

# y1 140,360,200,900

import numpy as np
import scipy.stats as stats

x1 = np.array([380,420, 290])

y1 = np.array([140,360,200,900])

result = stats.mannwhitneyu(x1, y1)

print(result)

# MannwhitneyuResult(statistic=8.0, pvalue=0.6285714285714286)  принимаем нулевую гипотезу, различий между выборками нет