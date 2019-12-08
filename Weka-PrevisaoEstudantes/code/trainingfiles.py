import os

for v in range(5,36):
	comando = 'java -cp weka.jar'
	comando += ' weka.classifiers.functions.MultilayerPerceptron -L 0.3 -M 0.2 -N 500 -V 0 -S 0 -E 20 -H a '
	comando += ' -t ./../data/arquivo-treino-auc/arqTreinoNumberAUC' + str(v) + '.arff'
	comando += ' -T ./../data/arquivo-teste-auc/arqTesteNumberAUC' + str(v) + '.arff'
	comando += ' -threshold-file ./../data/results-auc/situacao' + str(v) +'.arff -threshold-label fortemente_reprovado'
	comando += ' > ./../data/reports-auc/situacaoreport'+ str(v) +'.txt'

	os.system(comando)

