import os

for v in range(5,36):
	comando = 'java -cp weka.jar'
	comando += ' weka.classifiers.trees.HoeffdingTree -L 2 -S 1 -E 1.0E-7 -H 0.05 -M 0.01 -G 200.0 -N 0.0 '
	comando += ' -t ./../data/arquivo-treino-auc/arqTreinoNumberAUC' + str(v) + '.arff'
	comando += ' -T ./../data/arquivo-teste-auc/arqTesteNumberAUC' + str(v) + '.arff'
	comando += ' -threshold-file ./../data/results-hoeff/situacao' + str(v) +'.arff -threshold-label fortemente_reprovado'
	comando += ' > ./../data/reports-hoeff/situacaoreport'+ str(v) +'.txt'

	os.system(comando)




comando = 'java -cp weka.jar'
comando += ' weka.classifiers.trees.HoeffdingTree -L 2 -S 1 -E 1.0E-7 -H 0.05 -M 0.01 -G 200.0 -N 0.0 '
comando += ' -t ./../data/arqTreinoNumber.arff'
comando += ' -T ./../data/arqTesteNumber.arff'
comando += ' -threshold-file ./../data/results-hoeff/situacaoROCH.arff -threshold-label fortemente_reprovado'
comando += ' > ./../data/reports-hoeff/situacaoreportROC.txt'

os.system(comando)