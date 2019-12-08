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


roc_aucRNA = []
roc_aucNaive = []
roc_aucStump = []
roc_aucRegre = []
roc_aucHoeff = []

##Colhendo os os Dados do Naive
for i in range(5,50):
	dataRNA = arff.loadarff('/Users/rafaelandrade/Downloads/WekaFinal/data/results-auc/situacao' + str(i) +'.arff')
	dfRNA = pd.DataFrame(dataRNA[0])

	tprRNA = dfRNA['True Positive Rate']
	fprRNA = dfRNA['False Positive Rate']

	roc_aucRNA.append(metrics.auc(fprRNA, tprRNA))

##Colhendo os os Dados do Naive
for j in range(5,50):
	dataNaive = arff.loadarff('/Users/rafaelandrade/Downloads/WekaFinal/data/results-naive/situacao' + str(j) +'.arff')
	dfNaive = pd.DataFrame(dataNaive[0])

	tprNaive = dfNaive['True Positive Rate']
	fprNaive = dfNaive['False Positive Rate']

	roc_aucNaive.append(metrics.auc(fprNaive, tprNaive))

##Colhendo os os Dados do Stump
for h in range(5,50):
	dataStump = arff.loadarff('/Users/rafaelandrade/Downloads/WekaFinal/data/results-decisionstump/situacao' + str(h) +'.arff')
	dfStump = pd.DataFrame(dataStump[0])

	tprStump = dfStump['True Positive Rate']
	fprStump = dfStump['False Positive Rate']

	roc_aucStump.append(metrics.auc(fprStump, tprStump))

##Colhendo os os Dados do Regression
for v in range(5,50):
	dataRegre = arff.loadarff('/Users/rafaelandrade/Downloads/WekaFinal/data/results-classregre/situacao' + str(v) +'.arff')
	dfRegre = pd.DataFrame(dataRegre[0])

	tprRegre = dfRegre['True Positive Rate']
	fprRegre = dfRegre['False Positive Rate']

	roc_aucRegre.append(metrics.auc(fprRegre, tprRegre))

for y in range(5,50):
	dataHoeff = arff.loadarff('/Users/rafaelandrade/Downloads/WekaFinal/data/results-hoeff/situacao' + str(y) +'.arff')
	dfHoeff = pd.DataFrame(dataHoeff[0])

	tprHoeff = dfHoeff['True Positive Rate']
	fprHoeff = dfHoeff['False Positive Rate']

	roc_aucHoeff.append(metrics.auc(fprHoeff, tprHoeff))




aux = []
for z in range(5,50):
	aux.append(z)

plt.figure()
lw = 2
plt.plot(aux, roc_aucRNA, color='brown',
         lw=lw, label='RNA')
plt.plot(aux, roc_aucRegre, color='yellow',
         lw=lw, label='Classificação por Regressão')
plt.plot(aux, roc_aucStump, color='green',
         lw=lw, label='Decision Stump ')
plt.plot(aux, roc_aucNaive, color='black',
         lw=lw, label='Naive Bayes/Hoeffding')
plt.plot(aux, roc_aucHoeff, color='orange',
         lw=lw, label='Hoeffding')
#plt.fill_between(tpr, lower, upper, color='blue', alpha = 0.2)
plt.plot([5, 50], [0.5, 0.5], color='gray', lw=lw, linestyle='--', alpha = 0.5)
plt.xlim([5, 50])
plt.ylim([0.0, 1.0])
plt.xlabel('Número de Perguntas')
plt.ylabel('Valor do AUC')
plt.title('Valor do AUC dos Diferentes Algoritmos')
plt.legend(loc="lower right")
plt.show()


plt.figure()
lw = 2
plt.plot(aux, roc_auc, color='brown',
         lw=lw)
#plt.fill_between(tpr, lower, upper, color='blue', alpha = 0.2)
plt.plot([5, 50], [0.5, 0.5], color='black', lw=lw)
plt.axvline(x = 16, color = 'gray', linestyle='--', alpha = 0.5)
plt.plot([35],[roc_auc[30]], marker='o', markersize = 5, color = 'red')
plt.text(36 + 0.02,roc_auc[30] + 0.04, 'AUC = %0.4f' % roc_auc[30], fontsize = 10)
plt.axvline(x = 23, color = 'gray', linestyle='--', alpha = 0.5)
plt.plot([23],[roc_auc[18]], marker='s', markersize = 5, color = 'red')
plt.text(24 + 0.02,roc_auc[18] + 0.04, 'AUC = %0.4f' % roc_auc[18], fontsize = 10)
plt.axvline(x = 35, color = 'blue', linestyle='--', alpha = 0.5)
plt.axvline(x = 39, color = 'gray', linestyle='--', alpha = 0.5)
plt.xlim([5, 50])
plt.ylim([0.0, 1.0])
plt.xlabel('Número de Perguntas')
plt.ylabel('Valor do AUC')
plt.legend(loc="lower right")
plt.show()

