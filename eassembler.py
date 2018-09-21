def carregarOpcode(arquivo: str):
    file = open(arquivo, 'r')
    return file.readlines()


def carregarRegistradores(arquivo: str):
    file = open(arquivo, 'r')
    linhas = file.readlines()
    registradores = {}
    for pos, linha in enumerate(linhas):
        registradores[linha.replace('\n', '')] = pos
    return registradores


def carregarInstrucoes(arquivo: str):
    file = open(arquivo, 'r')
    linhas = file.readlines()
    instrucoes = {}
    for pos, linha in enumerate(linhas):
        linha = linha.split(';')
        linha = linha[0].replace('\t', '').strip()
        instrucoes[linha] = pos
    return instrucoes


def processamento(arquivo:str, registradores:dict,instrucoes:dict):
    file = open(arquivo,'r')
    linhas= file.readlines()
	linhaSaida=[]
	linhasSaida=[]
	for linha in linhas:
        #removendo a quebra de linha e os comentarios
		token = linha.replace('\n','').split(';')[0].replace(',',' ').strip().split(' ')
		print(token)
		if len(token)==3:
			if token[0].upper() == 'MOV':
				#MOV_MR ; mem <- reg
				#MOV_MI
				if token[1].upper() in registradores:
                    linhaSaida.append(instrucoes['MOV_RR'])
					linhaSaida.append(registradores[token[1].upper()])
					if token[2].upper() in registradores:
						#MOV_RR
						linhaSaida.append(registradores[token[2].upper()])
						#print(linhaSaida)
					if token[2][0]=='[' and token[2][len(token[2])-1]==']':
						#MOV_RM
						linhaSaida.append(int(token[2].replace('[','').replace(']','')))
					if str.isnumeric(token[2]):
						#MOV_RI
						linhaSaida.append(int(token[2]))
				print(linhaSaida)
                print(token)


def rawInputTreatment(entrada):
    #colocar cada linha da lista em um vetor separando por espaços e vigulas
    for linha in entrada:
        linha.rsplit(','' '';')


    return toAsmInterpreter

def asmInterpreter(asmCode, opCodes, regCodes):
    #Remover todos os comentários
    #While enquanto não encontrar o HALT
        #comparar "asmCode[x]" com "opCodes"
        #comparar "asmCode[x]" com "regCodes"
    #colocar tudo em uma matriz separando cada comando em uma linha
    #retornar essa matriz
    return toCompile

def inicio():
    arqReg = r'OPCODES.esym'
    arqIns = r'REGCODES.esym'
    arqEntrada = r'codigofonte.txt'

    '''arqReg = r'C:/Users/Andromeda/Assembler/REGCODES.esym'
    arqIns = r'C:/Users/Andromeda/Assembler/REGCODES.esym'
    arqEntrada = r'C:/Users/Andromeda/Assembler/codigofonte.txt'''

    '''arqReg = r'/home/grad/taac2017s2/igor.barreto/Trabalhos/Montador-Simulador/registradores.txt'
    arqIns = r'/home/grad/taac2017s2/igor.barreto/Trabalhos/Montador-Simulador/instrucoes.txt'
    arqEntrada = r'/home/grad/taac2017s2/igor.barreto/Trabalhos/Montador-Simulador/entrada.txt'''

    reg = carregarRegistradores(arqReg)
    inst = carregarInstrucoes(arqIns)
    # print(carregarOpcode(arqOpc))

    processamento(arqEntrada, reg, inst)


if __name__ == "__main__":
    inicio()