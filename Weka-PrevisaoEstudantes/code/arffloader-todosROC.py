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

##Colhendo os os Dados do Naive
dataRNA = arff.loadarff('/Users/rafaelandrade/Downloads/WekaFinal/data/results-number/Situation.arff')
dfRNA = pd.DataFrame(dataRNA[0])

tprRNA = dfRNA['True Positive Rate']
fprRNA = dfRNA['False Positive Rate']

roc_aucRNA = metrics.auc(fprRNA, tprRNA)

##Colhendo os os Dados do Naive
dataNaive = arff.loadarff('/Users/rafaelandrade/Downloads/WekaFinal/data/results-naive/situacaoROC.arff')
dfNaive = pd.DataFrame(dataNaive[0])

tprNaive = dfNaive['True Positive Rate']
fprNaive = dfNaive['False Positive Rate']

roc_aucNaive = metrics.auc(fprNaive, tprNaive)

##Colhendo os os Dados do Stump
dataStump = arff.loadarff('/Users/rafaelandrade/Downloads/WekaFinal/data/results-decisionstump/situacaoROC.arff')
dfStump = pd.DataFrame(dataStump[0])

tprStump = dfStump['True Positive Rate']
fprStump = dfStump['False Positive Rate']

roc_aucStump = metrics.auc(fprStump, tprStump)

##Colhendo os os Dados do Regression
dataRegre = arff.loadarff('/Users/rafaelandrade/Downloads/WekaFinal/data/results-classregre/situacaoROC.arff')
dfRegre = pd.DataFrame(dataRegre[0])

tprRegre = dfRegre['True Positive Rate']
fprRegre = dfRegre['False Positive Rate']

roc_aucRegre = metrics.auc(fprRegre, tprRegre)



print(roc_auc)

plt.figure()
lw = 2
plt.plot(fprNaive, tprNaive, color='brown',
         lw=lw, label='Naive Bayes/Hoeffding(AUC = %0.3f)' % roc_aucNaive)
plt.plot(fprStump, tprStump, color='yellow',
         lw=lw, label='Decision Stump (AUC = %0.3f)' % roc_aucStump)
plt.plot(fprRegre, tprRegre, color='green',
         lw=lw, label='Classificação por Regressão (AUC = %0.3f)' % roc_aucRegre)
plt.plot(fprRNA, tprRNA, color='black',
         lw=lw, label='RNA (AUC = %0.3f)' % roc_aucRNA)
#plt.fill_between(tpr, lower, upper, color='blue', alpha = 0.2)
plt.plot([0, 1], [0, 1], color='gray', lw=lw, linestyle='--', alpha = 0.5)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Taxa de Falsos Positivos')
plt.ylabel('Taxa de Verdadeiros Positivos')
plt.title('Curva ROC')
plt.legend(loc="lower right")
plt.show()