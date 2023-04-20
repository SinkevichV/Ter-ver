# Измерены значения IQ выборки студентов,
# обучающихся в местных технических вузах:

# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.

# Известно, что в генеральной совокупности IQ распределен нормально.

# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

import numpy as np
from statsmodels.stats.weightstats import _tconfint_generic as t_stat


X = np.array([131.0, 125.0, 115.0, 122.0, 131.0, 115.0, 107.0, 99.0, 125.0, 111.0])
mean_X = X.mean()
std_X = X.std(ddof=1)
mean_std_X = std_X / (np.sqrt(len(X)))

print(t_stat(mean_X, mean_std_X,len(X) - 1, 0.05, 'two-sided'))