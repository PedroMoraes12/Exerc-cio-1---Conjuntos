#NOME DO ALUNO: Pedro Henrique Moraes
#Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
#linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de
#operações que serão realizadas entre dois conjuntos de dados.
#O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
#contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
#em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
#segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
#operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
#seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
#operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
#terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
#das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
#4
#U
#3, 5, 67, 7
#1, 2, 3, 4
#I
#1, 2, 3, 4, 5
#4, 5
#D
#1, A, C, 34
#A, C, D, 23
#C
#3, 4, 5, 5, A, B, R
#1, B, C, D, 1

def main(arquivo_entrada):
    with open(arquivo_entrada, 'r') as file:
        linhas = file.readlines()

    num_operacoes = int(linhas[0].strip())

    index = 1

    for _ in range(num_operacoes):
        operacao = linhas[index].strip()

        conjunto1 = set(linhas[index + 1].strip().split(', '))
        conjunto2 = set(linhas[index + 2].strip().split(', '))

        if operacao == 'U':
            resultado = conjunto1.union(conjunto2)
            extenso = "UNIÃO"
        elif operacao == 'I':
            resultado = conjunto1.intersection(conjunto2)
            extenso = "INTERSEÇÃO"
        elif operacao == 'D':
            resultado = conjunto1.difference(conjunto2)
            extenso = "DIFERENÇA"
        elif operacao == 'C':
            resultado = {(x, y) for x in conjunto1 for y in conjunto2}
            extenso = "PRODUTO CARTESIANO"
        else:
            resultado = "OPERAÇÃO DESCONHECIDA"
            extenso = "ERRO"

        print(f"{extenso}: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}")

        index += 3
# ALTERAR O NOME PARA TESTAR OS OUTROS ARQUIVOS
main('entrada3.txt')
