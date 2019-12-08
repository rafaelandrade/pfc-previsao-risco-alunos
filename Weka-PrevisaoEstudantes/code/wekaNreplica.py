import pandas as pd
import os
import re

#reading files
path = '/Users/rafaelandrade/Downloads/Lógica 2019.1 01_03_2019-31_03_2019 .csv'
path2 = '/Users/rafaelandrade/Downloads/Lógica 2019.1 01_04_2019-30_04_2019 .csv'

def createTreinoReplies():
    return '/Users/rafaelandrade/Downloads/WekaFinal/data/arqTreinoReplies.arff'

def createTesteReplies():
    return '/Users/rafaelandrade/Downloads/WekaFinal/data/arqTesteReplies.arff'

def createTreinoNumber():
    return '/Users/rafaelandrade/Downloads/WekaFinal/data/arqTreinoNumber.arff'

def createTesteNumber():
    return '/Users/rafaelandrade/Downloads/WekaFinal/data/arqTesteNumber.arff'

#reading files of 2018
caminho = '/Users/rafaelandrade/Downloads/abril.csv'
caminho2 = '/Users/rafaelandrade/Downloads/maio.csv'

#reading files of 2019
file = pd.read_csv(path)
file2 = pd.read_csv(path2)

#reading files of 2018

file3 = pd.read_csv(caminho)
file4 = pd.read_csv(caminho2)

#delating some columns from files 2019
file = file.drop(["Card Number", "First name", "Last Name", "Score", "Correct", "Answered"], axis = 1)
file2 = file2.drop(["Card Number", "First name", "Last Name", "Score", "Correct", "Answered"], axis = 1)

#deleting some columns from files 2018
file3 = file3.drop(["Card Number", "First name", "Last Name", "Score", "Correct", "Answered"], axis = 1)
file4 = file4.drop(["Card Number", "First name", "Last Name", "Score", "Correct", "Answered"], axis = 1)

#creating a dictionary from file
file = file.to_dict()
file2 = file2.to_dict()
file3 = file3.to_dict()
file4 = file4.to_dict()

#head of file of 2019
head = list(file.keys())
head2 = list(file2.keys())

#head of file of 2018
head3 = list(file3.keys())
head4 = list(file4.keys())

#fullhead of 2019
fullHead = head + head2

#fullhead of 2018
fullHead2 = head3 + head4

notaRealFinal2018 = [3.4, 6.4, 0.6, 6.5, 6.1, 5.5, 2.1, 6.8, 1.7, 4.5, 4.3, 0.6, 8.3, 9.3, 9.5, 3.2, 7.1, 8.3, 8.5, 8.5, 4.6, 8.3, 6.8, 0.0, 6.0, 5.0, 9.1, 1.2, 5.3, 3.9, 7.4, 7.2, 6.8, 8.8, 7.6, 7.9, 8.0, 5.4, 7.7, 1.2, 6.0, 5.0, 1.4, 6.0, 6.0, 5.1, 7.8, 0.0, 4.7, 7.1]
notaRealFinal2019 = [2.8, 2.6, 10, 0, 8.2, 9.0, 7.2, 5.5, 7.5, 1.5, 8.2, 9.4, 0.7, 10, 9.9, 0, 10, 10, 8.1, 7.3, 9.8, 10, 10, 7.6, 0.3, 6, 6, 10, 3.9, 2.1, 4.5, 10, 0.6, 9, 7.5, 10, 10, 4, 10, 2.6, 9.5, 7.8, 3.5, 8.8, 7.9, 10, 7.4, 9.9, 10, 6.8]


with open(createTesteReplies(), 'w') as arquivoF:

        arquivoF.write('@relation teste\n\n\n')
        
        for j in range(len(fullHead)):
            if fullHead[j].endswith('.1') == False:
                arquivoF.write('@attribute questao_')
                arquivoF.write(str(j))
                arquivoF.write(" {'1', '0', '-1'}\n")
        

        arquivoF.write("@attribute situacao {'fortemente_aprovado', 'fortemente_reprovado'}\n")
        arquivoF.write('\n\n\n')
        arquivoF.write('@data\n')

        for aux in range(len(file[head[1]])):
            if aux != 0:
                for aux2 in range(len(head)):
                    if head[aux2].endswith('.1') == False:
                        if file[head[aux2]][0] == file[head[aux2]][aux]:
                            arquivoF.write("'")
                            arquivoF.write(str(1))
                            arquivoF.write("'")
                            arquivoF.write(",")
                        elif file[head[aux2]][aux] == '-':
                            arquivoF.write("'")
                            arquivoF.write(str(0))
                            arquivoF.write("'")
                            arquivoF.write(",")
                        else:
                            arquivoF.write("'")
                            arquivoF.write(str(-1))
                            arquivoF.write("'")
                            arquivoF.write(",")
                for aux3 in range(len(head2) - 4):
                    if head2[aux3].endswith('.1') == False:
                        if file2[head2[aux3]][0] == file2[head2[aux3]][aux]:
                            arquivoF.write("'")
                            arquivoF.write(str(1))
                            arquivoF.write("'")
                            arquivoF.write(",")
                        elif file2[head2[aux3]][aux] == '-':
                            arquivoF.write("'")
                            arquivoF.write(str(0))
                            arquivoF.write("'")
                            arquivoF.write(",")
                        else:
                            arquivoF.write("'")
                            arquivoF.write(str(-1))
                            arquivoF.write("'")
                            arquivoF.write(",")


                if notaRealFinal2019[aux-1] >= 6:
                    arquivoF.write("'")
                    arquivoF.write("fortemente_aprovado")
                    arquivoF.write("'")
                elif notaRealFinal2019[aux-1] >= 0 and notaRealFinal2019[aux-1] < 6:
                    arquivoF.write("'")
                    arquivoF.write("fortemente_reprovado")
                    arquivoF.write("'")
                arquivoF.write('\n')
arquivoF.close()


with open(createTreinoReplies(), 'w') as arquivoF:

        arquivoF.write('@relation teste\n\n\n')
        
        for j in range(len(fullHead2)):
            if fullHead2[j].endswith('.1') == False:
                arquivoF.write('@attribute questao_')
                arquivoF.write(str(j))
                arquivoF.write(" {'1', '0', '-1'}\n")
        

        arquivoF.write("@attribute situacao {'fortemente_aprovado', 'fortemente_reprovado'}\n")
        arquivoF.write('\n\n\n')
        arquivoF.write('@data\n')

        for aux in range(len(file[head[1]])):
            if aux != 0:
                for aux2 in range(len(head3)):
                    if head3[aux2].endswith('.1') == False:
                        if file3[head3[aux2]][0] == file3[head3[aux2]][aux]:
                            arquivoF.write("'")
                            arquivoF.write(str(1))
                            arquivoF.write("'")
                            arquivoF.write(",")
                        elif file3[head3[aux2]][aux] == '-':
                            arquivoF.write("'")
                            arquivoF.write(str(0))
                            arquivoF.write("'")
                            arquivoF.write(",")
                        else:
                            arquivoF.write("'")
                            arquivoF.write(str(-1))
                            arquivoF.write("'")
                            arquivoF.write(",")
                for aux3 in range(len(head2)):
                    if head4[aux3].endswith('.1') == False:
                        if file4[head4[aux3]][0] == file4[head4[aux3]][aux]:
                            arquivoF.write("'")
                            arquivoF.write(str(1))
                            arquivoF.write("'")
                            arquivoF.write(",")
                        elif file4[head4[aux3]][aux] == '-':
                            arquivoF.write("'")
                            arquivoF.write(str(0))
                            arquivoF.write("'")
                            arquivoF.write(",")
                        else:
                            arquivoF.write("'")
                            arquivoF.write(str(-1))
                            arquivoF.write("'")
                            arquivoF.write(",")




                if notaRealFinal2018[aux-1] >= 6:
                    arquivoF.write("'")
                    arquivoF.write("fortemente_aprovado")
                    arquivoF.write("'")
                elif notaRealFinal2018[aux-1] >= 0 and notaRealFinal2018[aux-1] < 6:
                    arquivoF.write("'")
                    arquivoF.write("fortemente_reprovado")
                    arquivoF.write("'")
                arquivoF.write('\n')
arquivoF.close()