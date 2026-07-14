# O Projeto: um panorama da família Flaviviridae
#
# Leia o enunciado completo no README (seção "O Projeto")
#
# A ideia é construir UMA tabela (pandas) descrevendo os vírus e, a partir dela,
# tirar duas conclusões:
#   - o conteúdo GC é aleatório? (Parte 2)
#   - quão grande é a proteína de cada vírus? (Parte 3)
#
# Vá preenchendo as partes abaixo, uma de cada vez.
# Obs: Se preferir fazer esse processo num jupyter notebook, sem problemas!! Fica a critério do grupo

import pandas as pd

pd.set_option('display.max_columns', None)   # mostra todas as colunas
pd.set_option('display.width', None)         # não quebra linha por largura do terminal
pd.set_option('display.max_colwidth', 60)    

from bio.ler_fasta import ler_fasta
from bio.sequencia import (
    traduzir,
    calcular_percentual_gc,
    encontrar_inicio,
)

# ------------------------------------------------------------------
# Parte 1 — Monte a tabela
# ------------------------------------------------------------------
organismos = ler_fasta("arquivos/Flaviviridae-genomes.fasta") # Lê o arquivo FASTA contendo as sequências genômicas da família Flaviviridae e armazena os dados em uma lista de dicionários chamada "organismos".
df = pd.DataFrame(organismos) # Cria um DataFrame do pandas chamado "df" a partir da lista de dicionários "organismos". Cada dicionário se torna uma linha no DataFrame, e as chaves dos dicionários se tornam os nomes das colunas.
df["tamanho"] = df["sequencia"].apply(len) # Cria uma nova coluna chamada "tamanho" no DataFrame "df". Essa coluna é preenchida aplicando a função len() a cada sequência na coluna "sequencia", calculando assim o comprimento (número de nucleotídeos) de cada sequência genômica. O resultado é armazenado na nova coluna "tamanho".
print(df.head())


# ------------------------------------------------------------------
# Parte 2 — O conteúdo GC é aleatório?
# ------------------------------------------------------------------
# 1) crie a coluna "gc" com df["sequencia"].apply(calcular_percentual_gc)
# 2) mostre os 10 maiores e os 10 menores GC (com o nome!) -> usar função sort_values do pandas
# 3) escreva sua conclusão sobre o padrão que observou


df["gc"] = df["sequencia"].apply(calcular_percentual_gc) # cria a coluna GC no dataframe, aplicando a função calcular_percentual_gc em cada sequência da coluna "sequencia"
df_sorted = df.sort_values(by="gc", ascending=False) # ordena o dataframe pelo valor da coluna "gc" em ordem decrescente (do maior para o menor)

print("10 maiores concentração GC:")
print(df_sorted.head(10)[["nome", "gc"]]) # exibe as 10 primeiras linhas do dataframe ordenado, mostrando apenas as colunas "nome" e "gc", que correspondem ao nome do vírus e à sua concentração de GC, respectivamente.

print("10 menores concentração GC:")
print(df_sorted.tail(10)[["nome", "gc"]]) # exibe as 10 últimas linhas do dataframe ordenado, mostrando apenas as colunas "nome" e "gc", que correspondem ao nome do vírus e à sua concentração de GC, respectivamente. Isso permite identificar os vírus com menor concentração de GC na família Flaviviridae.

print("\n--- Conclusão sobre o GC ---")
print("Os 10 vírus com maior GC são quase todos dos gêneros Pegivirus e Hepacivirus (incluindo Hepatitis C e GB virus).")
print("Os 10 com menor GC são majoritariamente Pestivirus.")
print("Isso mostra que o conteúdo GC não é distribuído ao acaso: ele está fortemente associado à linhagem evolutiva do vírus.")
print("Vírus de um mesmo gênero tendem a ter GC semelhante, sugerindo que pressões seletivas ou vieses mutacionais são conservados dentro de cada grupo.")
print("Portanto, o GC é um marcador que reflete a história evolutiva da família Flaviviridae.")

# ------------------------------------------------------------------
# Parte 3 — Encontre a proteína (a poliproteína viral)
# ------------------------------------------------------------------
# 1) coluna "proteina": traduzir(encontrar_inicio(seq), parar=True)
# 2) coluna "tamanho_proteina": len da proteína
# 3) coluna "cobertura": (tamanho_proteina * 3) / tamanho
# 4) escreva sua conclusão (qual a cobertura típica? faz sentido ser 1 poliproteína?)

df["seq_inicio"] = df["sequencia"].apply(encontrar_inicio) # Cria a coluna "seq_inicio" no DataFrame df aplicando a função encontrar_inicio em cada sequência da coluna "sequencia". Isso extrai a subsequência a partir do primeiro códon de start "ATG" para cada vírus e armazena o resultado na nova coluna "seq_inicio".
df["proteina"] = df["sequencia"].apply(lambda seq: traduzir(encontrar_inicio(seq), parar=True)) # Cria a coluna "proteina" no DataFrame df aplicando a função traduzir em cada sequência da coluna "seq_inicio". A função é chamada com o argumento parar=True para que a tradução pare no primeiro códon de parada encontrado. Isso gera a proteína correspondente à sequência viral e armazena o resultado na nova coluna "proteina".
df["tamanho_proteina"] = df["proteina"].apply(len) # Cria a coluna "tamanho_proteina" no DataFrame df aplicando a função len em cada sequência da coluna "proteina". Isso calcula o comprimento (número de aminoácidos) de cada proteína viral e armazena o resultado na nova coluna "tamanho_proteina".
df["cobertura"] = (df["tamanho_proteina"] * 3) / df["tamanho"] # Cria a coluna "cobertura" no DataFrame df calculando a proporção da sequência viral que é traduzida em proteína. A fórmula utilizada é (tamanho_proteina * 3) / tamanho, onde tamanho_proteina é o número de aminoácidos na proteína e tamanho é o comprimento total da sequência viral em nucleotídeos. Multiplicamos por 3 porque cada aminoácido é codificado por um códon de 3 nucleotídeos. O resultado é armazenado na nova coluna "cobertura".
cobertura_mediana = df["cobertura"].median() # calcula a mediana da coluna "cobertura"

# Vírus com cobertura < 0.3 (quantos são?)
baixa_cobertura = df[df["cobertura"] < 0.3][["nome", "cobertura", "tamanho"]] # Filtra o DataFrame df para obter apenas os vírus com cobertura menor que 0.3. A filtragem é feita utilizando a condição df["cobertura"] < 0.3, que seleciona as linhas onde a coluna "cobertura" é menor que 0.3. Em seguida, seleciona apenas as colunas "nome", "cobertura" e "tamanho" do DataFrame resultante, criando um novo DataFrame chamado baixa_cobertura que contém informações sobre os vírus com cobertura muito baixa.
print(f"\nVírus com cobertura < 0.3 ({len(baixa_cobertura)} ocorrências):")
print(baixa_cobertura)

# Vírus com cobertura > 0.9 (quantos são?)
alta_cobertura = df[df["cobertura"] > 0.9][["nome", "cobertura", "tamanho"]] # # Filtra o DataFrame df para obter apenas os vírus com cobertura maior que 0.9. A filtragem é feita utilizando a condição df["cobertura"] > 0.9, que seleciona as linhas onde a coluna "cobertura" é maior que 0.9. Em seguida, seleciona apenas as colunas "nome", "cobertura" e "tamanho" do DataFrame resultante, criando um novo DataFrame chamado alta_cobertura que contém informações sobre os vírus com cobertura muito alta.
print(f"\nVírus com cobertura > 0.9 ({len(alta_cobertura)} ocorrências):")
print(alta_cobertura)  

print("\n--- Conclusão sobre a proteína (poliproteína) ---")
print(f"A mediana da cobertura é {cobertura_mediana:.2f}, o que significa que, para a maioria dos vírus, a proteína traduzida ocupa cerca de 92% do genoma.")
print("Isso é fortemente consistente com o modelo biológico dos Flaviviridae: eles possuem uma única ORF (poliproteína) que cobre praticamente todo o genoma, restando apenas pequenas regiões não traduzidas (UTRs) nas extremidades.")
print("\n Observamos, porém, uma distribuição bimodal:")
print(f"  - {len(alta_cobertura)} vírus têm cobertura > 0.9, indicando genomas completos e bem anotados, onde a poliproteína ocupa quase todo o genoma.")
print(f"  - {len(baixa_cobertura)} vírus têm cobertura < 0.3, com valores muito baixos (muitos abaixo de 0.01).")
print("Isso sugere que esses genomas estão incompletos ou mal anotados, possivelmente devido a erros de sequenciamento ou regiões faltantes.")
print("Pode ter ocasionado stop codons prematuros ou ausência de regiões codificantes, resultando em proteínas truncadas ou inexistentes.")
      
# ------------------------------------------------------------------
# Parte 4 — Salve o resultado
# ------------------------------------------------------------------
# 1) filtre os vírus com gc > 0.5 (quantos são?)
# 2) df.to_csv("resultado.csv", index=False)

# Cria a lista de Verdadeiro/Falso (Filtro)
filtro = df["gc"] > 0.5

# Aplica a máscara para filtrar o DataFrame
filtro_gc = df[filtro]

print(f"\nNº de vírus com GC > 50% ({len(filtro_gc)} ocorrências):")
df.to_csv("resultado.csv", index=False)

