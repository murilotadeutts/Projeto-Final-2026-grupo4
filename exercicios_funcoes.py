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

sequencia = input("Digite a sequência de DNA: ").strip().upper()


def complementar(sequencia):
    """
    Retorna uma NOVA string com a sequência complementar.

    Lembre-se do pareamento das bases: A<->T e C<->G.
    Ex: complementar("ATCG") -> "TAGC"

    Dica: percorra cada base da sequência e vá montando (concatenando)
    a sequência complementar numa nova string.
    """


    from bio.constantes import CONVERSOR_DE_BASE
    sequencia = sequencia.upper()
    sequencia_complementar = ""

    for base in sequencia:
        sequencia_complementar = sequencia_complementar + CONVERSOR_DE_BASE [base]
        
    return sequencia_complementar

print(complementar(sequencia))

# 2) complementar_reversa — esperado: "CGAT"
# print(complementar_reversa("ATCG"))

def complementar_reversa(sequencia):
    comp=complementar(sequencia)
    return comp[::-1]

print(complementar_reversa(sequencia))

# 3) transcrever          — esperado: "AUCG"
# print(transcrever("ATCG"))


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


# 6) calcular_percentual  — esperado: 0.5 (metade das bases é A)
# print(calcular_percentual("ATCGAAAA", ["A"]))


# 7) calcular_percentual_gc — esperado: ~0.66 (4 Cs/Gs em 6 bases)
# print(calcular_percentual_gc("ATCGCC"))
def calcular_percentual_gc(sequencia):
    g_count = sequencia.count("G")  # Conta o número de ocorrências da base "G" na sequência.
    c_count = sequencia.count("C")  # Conta o número de ocorrências da base "C" na sequência.
    total_bases = len(sequencia)  # Calcula o comprimento total da sequência.
    
    gc_content = (g_count + c_count) / total_bases  # Calcula o percentual de GC somando as contagens de G e C e dividindo pelo total de bases.
    return gc_content  

print(calcular_percentual_gc("ATGC")) 


# 8) contar_bases         — esperado: {"A": 2, "T": 1, "C": 1, "G": 1}
# print(contar_bases("ATCGA"))
