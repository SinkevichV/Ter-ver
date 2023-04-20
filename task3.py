# Известно, что рост футболистов в сборной распределен нормально с дисперсией генеральной совокупности, 
# равной 25 кв.см. Объем выборки равен 27, среднее выборочное составляет 174.2. 
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

import numpy as np
from statsmodels.stats.weightstats import _tconfint_generic as t_stat

mean_X = 174.2
std_X = np.sqrt(25)
mean_std_X = std_X / np.sqrt(27)

print(t_stat(mean_X, mean_std_X,27 - 1, 0.05, 'two-sided'))