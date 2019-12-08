import os

for v in range(5,36):
	comando = 'java -cp weka.jar'
	comando += ' weka.classifiers.trees.DecisionStump '
	comando += ' -t ./../data/arquivo-treino-auc/arqTreinoNumberAUC' + str(v) + '.arff'
	comando += ' -T ./../data/arquivo-teste-auc/arqTesteNumberAUC' + str(v) + '.arff'
	comando += ' -threshold-file ./../data/results-decisionstump/situacao' + str(v) +'.arff -threshold-label fortemente_reprovado'
	comando += ' > ./../data/reports-decisionstump/situacaoreport'+ str(v) +'.txt'

	os.system(comando)




comando = 'java -cp weka.jar'
comando += ' weka.classifiers.trees.DecisionStump '
comando += ' -t ./../data/arqTreinoNumber.arff'
comando += ' -T ./../data/arqTesteNumber.arff'
comando += ' -threshold-file ./../data/results-decisionstump/situacaoROC.arff -threshold-label fortemente_reprovado'
comando += ' > ./../data/reports-decisionstump/situacaoreportROC.txt'

os.system(comando)