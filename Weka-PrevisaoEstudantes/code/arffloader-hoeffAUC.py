from scipy.io import arff
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
import statistics
from fractions import Fraction as F
from decimal import Decimal as D


roc_auc = []

for i in range(5,36):
	data = arff.loadarff('/Users/rafaelandrade/Downloads/WekaFinal/data/results-hoeff/situacao' + str(i) +'.arff')
	df = pd.DataFrame(data[0])

	tpr = df['True Positive Rate']
	fpr = df['False Positive Rate']

	roc_auc.append(metrics.auc(fpr, tpr))

aux = []
for i in range(5,36):
	aux.append(i)

plt.figure()
lw = 2
plt.plot(aux, roc_auc, color='brown',
         lw=lw)
#plt.fill_between(tpr, lower, upper, color='blue', alpha = 0.2)
plt.plot([5, 36], [0.5, 0.5], color='black', lw=lw)
plt.axvline(x = 16, color = 'gray', linestyle='--', alpha = 0.5)
plt.plot([35],[roc_auc[30]], marker='o', markersize = 5, color = 'red')
plt.text(30 + 0.02,roc_auc[30] + 0.04, 'AUC = %0.4f' % roc_auc[30], fontsize = 10)
plt.axvline(x = 23, color = 'gray', linestyle='--', alpha = 0.5)
plt.plot([23],[roc_auc[18]], marker='s', markersize = 5, color = 'red')
plt.text(19 + 0.02,roc_auc[18] + 0.04, 'AUC = %0.4f' % roc_auc[18], fontsize = 10)
plt.axvline(x = 35, color = 'blue', linestyle='--', alpha = 0.5)
plt.xlim([5, 36])
plt.ylim([0.0, 1.0])
plt.xlabel('Número de Perguntas')
plt.ylabel('Valor do AUC')
plt.legend(loc="lower right")
plt.show()





