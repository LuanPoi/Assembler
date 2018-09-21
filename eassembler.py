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


def processamento(arquivo: str, registradores: dict, instrucoes: dict):
    file = open(arquivo, 'r')
    linhas = file.readlines()
    linhasSaida = []
    print(linhas)
    print("--##--##-- Debug --##--##--")
    for linha in linhas:
        # removendo a quebra de linha e os comentarios
        token = linha.splitlines()
        token[0] = token[0].split(' ')
        #token[0] = token[0].split(',')
        #token[0] = token[0].split(';')
        print(token)
        if len(token) == 1:
            if token[0].upper() in instrucoes.keys():
                linhaSaida.append(instrucoes[token[0].upper()])
                pass


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
    arqReg = r'C:/Users/Andromeda/Assembler/REGCODES.esym'
    arqIns = r'C:/Users/Andromeda/Assembler/REGCODES.esym'
    arqEntrada = r'C:/Users/Andromeda/Assembler/codigofonte.txt'

    '''arqReg = r'/home/grad/taac2017s2/igor.barreto/Trabalhos/Montador-Simulador/registradores.txt'
    arqIns = r'/home/grad/taac2017s2/igor.barreto/Trabalhos/Montador-Simulador/instrucoes.txt'
    arqEntrada = r'/home/grad/taac2017s2/igor.barreto/Trabalhos/Montador-Simulador/entrada.txt'''

    reg = carregarRegistradores(arqReg)
    inst = carregarInstrucoes(arqIns)
    # print(carregarOpcode(arqOpc))

    processamento(arqEntrada, reg, inst)


if __name__ == "__main__":
    inicio()