# 3 ) Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было.

import numpy as np
import scipy.stats as stats


x1 = np.array([150, 160, 165, 145, 155])

x2 = np.array([140, 155, 150,  130, 135])


result = stats.wilcoxon(x1, x2)
print(result)

# WilcoxonResult(statistic=0.0, pvalue=0.0625)  статистически значимыx различий нет!