import random

class Sapeca:
    combinacoesGeradas = []
    
    def __init__(self, quantidadeCifras, tamanhoCifras, letras, tipoLetras, numeros, caracteresEspeciais):
        self.quantidadeCifras = quantidadeCifras
        self.tamanhoCifras = tamanhoCifras
        self.letras = letras
        self.tipoLetras = tipoLetras
        self.numeros = numeros
        self.caracteresEspeciais = caracteresEspeciais
    
    def criaCombinacoes(self):
 
        print("Criando cifras...\n")
        letrasMinusculas = 'abcdefghijklmnopqrstuvwxyz'
        letrasMaiusculas = letrasMinusculas.upper()
        numeros = '0123456789'
        caracteresEspeciais = '!@#$%^&*`´~'
        
        opcoes = []
        if self.tipoLetras == 'minúsculas':
            opcoes.append(letrasMinusculas)
        elif self.tipoLetras == 'maiúsculas':
            opcoes.append(letrasMaiusculas)
        else:
            opcoes.append(letrasMinusculas)
            opcoes.append(letrasMaiusculas)
        
        if self.numeros:
            opcoes.append(numeros)
 
        if self.caracteresEspeciais:
            opcoes.append(caracteresEspeciais)

        random.shuffle(opcoes)

        for _ in range(self.quantidadeCifras):
            combinacao = ''
            for _ in range(self.tamanhoCifras):
                opcao = random.choice(opcoes)
                combinacao += random.choice(opcao)

            self.combinacoesGeradas.append(combinacao)
    
    def __str__(self):
        result = ""
        for i, combinacao in enumerate(self.combinacoesGeradas, 1):
            result += f"{i}. {combinacao}\n"
        result += "\nSAPECA-IAIÁ!\n"
        return result
            

def verificaResposta(resposta):
    return resposta.lower() in ['s', 'y']

def interpretaLetras(verificaTipoLetras):
    if verificaTipoLetras == "1":
        tipoLetras = 'maiúsculas'
        return tipoLetras
    elif verificaTipoLetras == "2":
        tipoLetras = 'minúsculas'
        return tipoLetras
    else:
        tipoLetras = 'ambas'
        return tipoLetras

print("Boas-vindas ao S.A.P.E.C.A (Sistema Algorítmico para Produção Exclusiva de Combinações Aleatórias)™!")
print("O objetivo deste pequeno sistema é te ajudar a gerar cifras aleatórias que podem servir como senhas superdifíceis de se descobrir para proteger suas contas virtuais, por exemplo.")

quantidadeCifras = int(input("A princípio, quantas cifras você deseja gerar?\n"))
tamanhoCifras = int(input("Adiante, qual o tamanho que você deseja que as cifras possuam?\n"))

teraLetras = input("Você deseja que as cifras possuam letras? S/N\n")
letras = verificaResposta(teraLetras)

if (letras):
    verificaTipoLetras = input("Você deseja que essas letras sejam: 1: maiúsculas, 2: minúsculas ou qualquer outra tecla para ambas?\n")
    tipoLetras = interpretaLetras(verificaTipoLetras)
        
teraNumeros = input("Você deseja que as cifras possuam números? S/N\n")
numeros = verificaResposta(teraNumeros)

teraCaracteresEspeciais = input("Você deseja que as cifras possuam caracteres especiais? S/N\n")
caracteresEspeciais = verificaResposta(teraCaracteresEspeciais)

sapequento = Sapeca(quantidadeCifras, tamanhoCifras, letras, tipoLetras, numeros, caracteresEspeciais)
sapequento.criaCombinacoes()

print(sapequento)