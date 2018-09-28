def carregarOpcode(arquivo: str):
    file = open(arquivo, 'r')
    linhas = file.readlines()
    opcode = tratarOpcode(linhas)
    return opcode

def tratarOpcode(linhas: list):
    operadores = {}
    valor = 0
    for linha, instrucao in enumerate(linhas):
        instrucao = instrucao.split(';')
        instrucao = instrucao[0].replace('\t', '').strip()
        if instrucao != "":
            operadores[instrucao.replace('\n', '')] = valor
            valor = valor+1
    return operadores

def carregarRegistradores(arquivo: str):
    file = open(arquivo, 'r')
    linhas = file.readlines()
    registradores = {}
    for linha, instrucao in enumerate(linhas):
        registradores[instrucao.replace('\n', '')] = linha
    return registradores


def carregarInstrucoes(arquivo: str):
    file = open(arquivo, 'r')
    linhas = file.readlines()
    return linhas


#def processamento(arquivo:str, registradores:dict,instrucoes:dict):
#     file = open(arquivo,'r')
#     linhas= file.readlines()
# 	linhaSaida=[]
# 	linhasSaida=[]
# 	for linha in linhas:
#         #removendo a quebra de linha e os comentarios
# 		token = linha.replace('\n','').split(';')[0].replace(',',' ').strip().split(' ')
# 		print(token)
# 		if len(token)==3:
# 			if token[0].upper() == 'MOV':
# 				#MOV_MR ; mem <- reg
# 				#MOV_MI
# 				if token[1].upper() in registradores:
#                     linhaSaida.append(instrucoes['MOV_RR'])
# 					linhaSaida.append(registradores[token[1].upper()])
# 					if token[2].upper() in registradores:
# 						#MOV_RR
# 						linhaSaida.append(registradores[token[2].upper()])
# 						#print(linhaSaida)
# 					if token[2][0]=='[' and token[2][len(token[2])-1]==']':
# 						#MOV_RM
# 						linhaSaida.append(int(token[2].replace('[','').replace(']','')))
# 					if str.isnumeric(token[2]):
# 						#MOV_RI
# 						linhaSaida.append(int(token[2]))
# 				print(linhaSaida)
#                 print(token)

#def tratarOPCODE (listaOpc: list):

def tratarEntrada(linhas: list):
    # colocar cada linha da lista em um vetor separando por espaços e vigulas e remove comentarios
    instrucoes = []

    dado = []
    for linha, dado in enumerate(linhas):
        instrucao = []
        dado = dado.split(';')
        dado = dado[0].replace('\t', '').strip()
        dado = dado.upper()

        if dado == "":    # Remove as linhas vazias
            continue
        dado = dado.split(' ')
        instrucao.append(dado[0])
        if len(dado) >= 2:
            dado = dado[1].split(',')
            instrucao.append(dado[0])
            if len(dado) >= 2:
                instrucao.append(dado[1])


        instrucoes.append(instrucao.copy())

        if dado[0] == "HALT":
            break

    return instrucoes

#def (asmCode, opCodes, regCodes):


def inicio():
    arqReg = r'REGCODES.esym'
    arqOpc = r'OPCODES.esym'
    arqEntrada = r'codigofonte.txt'

    '''arqReg = r'/home/grad/taac2017s2/igor.barreto/Trabalhos/Montador-Simulador/registradores.txt'
    arqIns = r'/home/grad/taac2017s2/igor.barreto/Trabalhos/Montador-Simulador/instrucoes.txt'
    arqEntrada = r'/home/grad/taac2017s2/igor.barreto/Trabalhos/Montador-Simulador/entrada.txt'''

    reg = carregarRegistradores(arqReg)
    op = carregarOpcode(arqOpc)
    entrada = carregarInstrucoes(arqEntrada)

    entrada = tratarEntrada(entrada)

    print(reg)  # DEBUG
    print("----------------------")  # DEBUG
    print(op)  # DEBUG
    print("----------------------")  # DEBUG
    for instrucao in entrada:   # DEBUG
        print(instrucao)  # DEBUG

if __name__ == "__main__":
    inicio()