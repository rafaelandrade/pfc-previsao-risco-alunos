import os

for v in range(5,36):
	comando = 'java -cp weka.jar'
	comando += ' weka.classifiers.bayes.NaiveBayes '
	comando += ' -t ./../data/arquivo-treino-auc/arqTreinoNumberAUC' + str(v) + '.arff'
	comando += ' -T ./../data/arquivo-teste-auc/arqTesteNumberAUC' + str(v) + '.arff'
	comando += ' -threshold-file ./../data/results-naive/situacao' + str(v) +'.arff -threshold-label fortemente_reprovado'
	comando += ' > ./../data/reports-naive/situacaoreport'+ str(v) +'.txt'

	os.system(comando)




comando = 'java -cp weka.jar'
comando += ' weka.classifiers.bayes.NaiveBayes '
comando += ' -t ./../data/arqTreinoNumber.arff'
comando += ' -T ./../data/arqTesteNumber.arff'
comando += ' -threshold-file ./../data/results-naive/situacaoROC.arff -threshold-label fortemente_reprovado'
comando += ' > ./../data/reports-naive/situacaoreportROC.txt'

os.system(comando)