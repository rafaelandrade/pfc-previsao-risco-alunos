import os

for v in range(5,36):
	comando = 'java -cp weka.jar'
	comando += ' weka.classifiers.meta.ClassificationViaRegression '
	comando += ' -t ./../data/arquivo-treino-auc/arqTreinoNumberAUC' + str(v) + '.arff'
	comando += ' -T ./../data/arquivo-teste-auc/arqTesteNumberAUC' + str(v) + '.arff'
	comando += ' -threshold-file ./../data/results-classregre/situacao' + str(v) +'.arff -threshold-label fortemente_reprovado'
	comando += ' > ./../data/reports-classregre/situacaoreport'+ str(v) +'.txt'

	os.system(comando)




comando = 'java -cp weka.jar'
comando += ' weka.classifiers.meta.ClassificationViaRegression '
comando += ' -t ./../data/arqTreinoNumber.arff'
comando += ' -T ./../data/arqTesteNumber.arff'
comando += ' -threshold-file ./../data/results-classregre/situacaoROC.arff -threshold-label fortemente_reprovado'
comando += ' > ./../data/reports-classregre/situacaoreportROC.txt'

os.system(comando)