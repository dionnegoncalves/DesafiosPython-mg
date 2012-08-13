from operator import itemgetter
from collections import Counter

def problema(filename):
    with open(filename) as arq:
        conteudo = arq.read().split()
        nomes = conteudo[::2]
        idades = conteudo[1::2]
        if len(nomes) != len(idades):
            raise IOError
        if conteudo:
            tuplas = [(nome,int(idade)) for nome,idade in zip(nomes,idades)]
            tuplas.sort(key=itemgetter(1,0))
            print tuplas[0][0]
            print tuplas[-1][0]
            print dict(Counter(idades))



#problema('teste0.txt')
#problema('teste4.txt') 
print('2:')
problema('teste2.txt')
print('3:')
problema('teste3.txt')
print('1:')
problema('teste1.txt')
print('5:')
problema('teste5.txt')
print('6:')
problema('teste6.txt')
