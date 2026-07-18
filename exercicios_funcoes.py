# Exercícios das funções
#
# Aqui você testa CADA função que criou em bio/sequencia.py, isoladamente,
# numa sequência pequena, para conferir que todas funcionam.
#
# Leia o enunciado no README (seção "Exercícios das funções").
#
# Para cada bloco abaixo, escreva um print mostrando o resultado e confira se
# bate com o esperado no comentário.

from bio.sequencia import (
    complementar,
    complementar_reversa,
    transcrever,
    traduzir,
    calcular_percentual,
    calcular_percentual_gc,
    contar_bases,
    encontrar_inicio,
)


# 1) complementar        — esperado: "TAGC"
# print(complementar("ATCG"))

def complementar(sequencia):
 
    from bio.constantes import CONVERSOR_DE_BASE

    sequencia_complementar = "" 

    for base in sequencia: 
        sequencia_complementar = sequencia_complementar + CONVERSOR_DE_BASE [base] # Adiciona o complemento da base atual à sequência complementar, utilizando o dicionário CONVERSOR_DE_BASE para obter o par complementar correto.
        
    return sequencia_complementar

print(complementar("ATCG"))

# 2) complementar_reversa — esperado: "CGAT"
# print(complementar_reversa("ATCG"))

def complementar_reversa(sequencia):
    comp=complementar(sequencia) # Obtém a sequência complementar chamando a função complementar() com a sequência original como argumento.
    return comp[::-1] # Retorna a sequência complementar invertida, utilizando fatiamento [::-1] para reverter a ordem dos caracteres na string. Isso produz a sequência complementar reversa desejada.

print(complementar_reversa("ATCG"))

# 3) transcrever          — esperado: "AUCG"
# print(transcrever("ATCG"))

def transcrever(sequencia):
    rna = sequencia.replace("T", "U") # Substitui todas as ocorrências da base T (timina) por U (uracila) na sequência de DNA, utilizando o método replace() da string.
    return rna # Retorna a sequência de RNA resultante após a substituição.

print(transcrever("ATCG"))

# 4) encontrar_inicio     — esperado: "ATGGGGTAA" (começa no 1º ATG)
# print(encontrar_inicio("CCCATGGGGTAA"))

def encontrar_inicio(sequencia):
    posicao_start = sequencia.find("ATG")  # Utiliza o método find() para localizar a posição do primeiro códon de start "ATG" na sequência. Se não encontrar, retorna -1.
    if posicao_start != -1:  # Verifica se o códon de start foi encontrado (posição diferente de -1).
        return sequencia[posicao_start:]  # Retorna a sequência a partir do códon de start encontrado, utilizando fatiamento.
    else:
        return ""  # Retorna uma string vazia se nenhum códon de start for encontrado.

print(encontrar_inicio("CCCATGGGGTAA"))


# 5) traduzir             — esperado: "MAIVMGR*KGAR*"
# print(traduzir("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"))

#    traduzir com parar=True — deve PARAR no primeiro stop codon, esperado: "MAIVMGR"
# print(traduzir("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", parar=True))

def traduzir(sequencia, parar=True):
    
    from bio.constantes import DNA_PARA_AMINOACIDO, DNA_STOP_CODONS

    proteina = ""  

    for i in range(0, len(sequencia), 3):  # Itera sobre a sequência em passos de 3, para pegar cada códon.
        codon = sequencia[i:i+3]  # Extrai o códon atual (trinca de bases) da sequência.

        if codon in DNA_STOP_CODONS:  # Verifica se o códon é um stop codon.
            proteina += "*"  # Adiciona "*" à proteína para indicar o stop codon.
            if parar:  # Se a opção de parar no primeiro stop codon estiver ativada,
                break  # interrompe a tradução e sai do loop.
        elif codon in DNA_PARA_AMINOACIDO:  # Verifica se o códon está no dicionário de tradução.
            proteina += DNA_PARA_AMINOACIDO[codon]  # Adiciona o aminoácido correspondente à proteína.
        else:
            proteina += "X"  # Se o códon não estiver no dicionário, adiciona "X" para indicar base indefinida.

    return proteina 

print (traduzir("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"))


# 6) calcular_percentual  — esperado: 0.5 (metade das bases é A)
# print(calcular_percentual("ATCGAAAA", ["A"]))

def calcular_percentual(sequencia, bases):
    tamanho_da_sequencia = len(sequencia) # Calcula o comprimento total da sequência.
    contagem = 0 # Inicializa a variável contagem para contar quantas bases da sequência estão na lista fornecida.
    for base in sequencia:
        if base == bases: # Verifica se a base atual está na lista de bases fornecida.
            contagem += 1 # Incrementa a contagem se a base estiver na lista.
            
    percentual = contagem / tamanho_da_sequencia # Calcula o percentual de bases encontradas dividindo a contagem pelo comprimento total da sequência.
    return percentual

print(calcular_percentual("ATCGTAAA", "A"))

# 7) calcular_percentual_gc — esperado: ~0.66 (4 Cs/Gs em 6 bases)
# print(calcular_percentual_gc("ATCGCC"))

def calcular_percentual_gc(sequencia):
    g_count = sequencia.count("G")  # Conta o número de ocorrências da base "G" na sequência.
    c_count = sequencia.count("C")  # Conta o número de ocorrências da base "C" na sequência.
    total_bases = len(sequencia)  # Calcula o comprimento total da sequência.
    
    gc_content = (g_count + c_count) / total_bases  # Calcula o percentual de GC somando as contagens de G e C e dividindo pelo total de bases.
    return gc_content  

print(calcular_percentual_gc("ATCGCC")) 


# 8) contar_bases         — esperado: {"A": 2, "T": 1, "C": 1, "G": 1}
# print(contar_bases("ATCGA"))

def contar_bases(sequencia):
    contagem = { # Inicializa um dicionário chamado contagem com as bases A, T, C e G, todas com valor inicial 0. Isso servirá para armazenar a contagem de cada base na sequência fornecida.
        "A": 0,
        "T": 0,
        "C": 0,
        "G": 0
    }

    for base in sequencia:
        contagem[base] += 1 # Incrementa a contagem da base atual no dicionário contagem. Para cada base na sequência, o valor correspondente no dicionário é aumentado em 1.

    return contagem

print(contar_bases("ATCGA"))
