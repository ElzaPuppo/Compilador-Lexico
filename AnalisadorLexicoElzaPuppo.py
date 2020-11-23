import re
import string

arq = open('lista.txt', 'r')
conteudo = arq.read()

conteudo = conteudo.replace('\n', ' \n ')
nconteudo = conteudo.split(' ')

limite = len(nconteudo)


def reservada(palavra):

    retorno = '1'
    if palavra == "<":
        retorno = 'lessthan'
    elif palavra == '>':
        retorno = 'morethan'
    elif palavra == '<>':
        retorno = 'dif'
    elif palavra == '=' :
        retorno = 'equal'
    elif palavra == ';':
        retorno = 'scolon'
    elif palavra == 'ou':
        retorno = 'Or'
    elif palavra == '>=':
        retorno = 'moreequal'
    elif palavra == '<=':
        retorno = 'lessequal'
    elif palavra == 'fim':
        retorno = 'End'
    elif palavra == 'inicio':
        retorno = 'Start'
    elif palavra == 'programa':
        retorno = 'Prog'
    elif palavra == 'se':
        retorno = 'If'
    elif palavra == 'então':
        retorno = 'Then'
    elif palavra == 'senão':
        retorno = 'Else'
    elif palavra == ':=':
        retorno = 'equals'
    elif palavra == 'enquanto':
        retorno = 'While'
    elif palavra == 'faca':
        retorno = 'Do'
    elif palavra == 'leia':
        retorno = 'Read'
    elif palavra == 'escreva':
        retorno = 'Write'
    elif palavra == 'div':
        retorno = 'Div'
    elif palavra == 'e':
        retorno = 'And'
    elif palavra == 'verdadeiro':
        retorno = 'True'
    elif palavra == 'falso':
        retorno = 'False'
    elif palavra == 'nao':
        retorno = 'Not'
    elif palavra == 'id':
        retorno = 'Id'
    elif palavra == 'num':
        retorno = 'Num'
    elif palavra == '*':
        retorno = 'Mult'
    elif palavra == '+':
        retorno = 'Plus'
    elif palavra == '-':
        retorno = 'Less'
    elif palavra == ')':
        retorno = 'Close'
    elif palavra == '(':
        retorno = 'Open'
    else:
        retorno = '0'
      
    return retorno

def atribui(palavra,linha):
    
    retorno = '0'
    
    if palavra.isnumeric():
        retorno = 'num'
        
    elif reservada(palavra) != '0':
        retorno = reservada(palavra)

    elif palavra.isalpha():
        retorno = 'ident'

    else:
        retorno = 'error'
        print("Erro em linha ",linha)

    return retorno

pos = 0
prov = 0
linha = 1
postab = 0
excluir = 0
posdelete = 0

while posdelete<limite:

    if nconteudo[posdelete] == '\n':
        excluir = excluir +1
    posdelete = posdelete+1

tabelafinal = []

for i in range(limite-excluir):
    tabelafinal.append( [0] * 3 )


      

while pos<limite:

    if nconteudo[pos] == '\n':
        linha = linha +1
        

    else:
        tabelafinal[postab][0]= nconteudo[pos]
        tabelafinal[postab][1]= atribui(nconteudo[pos],linha)
        tabelafinal[postab][2] = linha
        postab= postab+1

    pos = pos +1


tabelaconvertida = str(tabelafinal).strip(' ')
cont = 0
lim = len(tabelaconvertida) -1
arq = open('Table.txt', 'w')
arq.write("Cont - ID - Line")
arq.write("\n")
while cont< lim:
    if tabelaconvertida[cont] == ']' and tabelaconvertida[cont+1] == ',':        
        arq.write("\n")
        cont = cont+2
    elif tabelaconvertida[cont] == '[' or tabelaconvertida[cont] == ']':
        cont = cont +1
    else:
        arq.write(tabelaconvertida[cont])
        cont = cont +1
arq.close()







