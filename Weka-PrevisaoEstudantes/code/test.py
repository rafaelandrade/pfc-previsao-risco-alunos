import os


comando = 'java -cp weka.jar'
comando += ' weka.classifiers.functions.MultilayerPerceptron -L 0.3 -M 0.2 -N 200 -V 0 -S 0 -E 20 -H a '
comando += ' -t ./../data/arqTreino.arff'
comando += ' -T ./../data/arqTeste.arff'
comando += ' -threshold-file ./../data/results/Situation.arff -threshold-label fortemente_reprovado'
comando += ' > ./../data/reports/SituationReport.txt'

os.system(comando)



comando = 'java -cp weka.jar'
comando += ' weka.classifiers.functions.MultilayerPerceptron -L 0.3 -M 0.2 -N 200 -V 0 -S 0 -E 20 -H a '
comando += ' -t ./../data/arqTreinoNumber.arff'
comando += ' -T ./../data/arqTesteNumber.arff'
comando += ' -threshold-file ./../data/results-number/Situation.arff -threshold-label fortemente_reprovado'
comando += ' > ./../data/reports-number/SituationReport.txt'

os.system(comando)


