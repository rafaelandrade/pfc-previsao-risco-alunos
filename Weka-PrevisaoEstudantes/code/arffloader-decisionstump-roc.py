
from scipy.io import arff
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
import statistics
import scipy.stats
from fractions import Fraction as F
from decimal import Decimal as D
plt.style.use('ggplot')

def ci(data, fpr, confidence = 0.95):
	a = 1.0 * np.array(data)
	n = len(a)
	m, se = np.mean(a), scipy.stats.sem(a)
	h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
	lower = []
	upper = []
	for i in range(len(fpr)):
		lower.append(fpr[i]  - h)
		upper.append(fpr[i]  + h)
	return lower, upper


roc_auc = []

base = np.linspace(0, 1, 51)


data = arff.loadarff('/Users/rafaelandrade/Downloads/WekaFinal/data/results-decisionstump/situacaoROC.arff')
df = pd.DataFrame(data[0])

tpr = df['True Positive Rate']
fpr = df['False Positive Rate']

roc_auc = metrics.auc(fpr, tpr)


#lower, upper = ci(tpr, fpr)

print(roc_auc)

plt.figure()
lw = 2
plt.plot(fpr, tpr, color='brown',
         lw=lw, label='Curva ROC (area = %0.3f)' % roc_auc)
#plt.fill_between(tpr, lower, upper, color='blue', alpha = 0.2)
plt.plot([0, 1], [0, 1], color='gray', lw=lw, linestyle='--', alpha = 0.5)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Taxa de Falsos Positivos')
plt.ylabel('Taxa de Verdadeiros Positivos')
plt.title('Curva ROC')
plt.legend(loc="lower right")
plt.show()