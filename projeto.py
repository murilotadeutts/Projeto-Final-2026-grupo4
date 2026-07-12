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
organismos = ler_fasta("arquivos/Flaviviridae-genomes.fasta")
df = pd.DataFrame(organismos)
df["tamanho"] = df["sequencia"].apply(len)
print(df.head())


# ------------------------------------------------------------------
# Parte 2 — O conteúdo GC é aleatório?
# ------------------------------------------------------------------
# 1) crie a coluna "gc" com df["sequencia"].apply(calcular_percentual_gc)
# 2) mostre os 10 maiores e os 10 menores GC (com o nome!) -> usar função sort_values do pandas
# 3) escreva sua conclusão sobre o padrão que observou


df["gc"] = df["sequencia"].apply(calcular_percentual_gc) # cria a coluna GC no dataframe, aplicando a função calcular_percentual_gc em cada sequência da coluna "sequencia"
df_sorted = df.sort_values(by="gc", ascending=False) # ordena o dataframe pelo valor da coluna "gc" em ordem decrescente (do maior para o menor)
print("10 maiores concentração CG:")
print(df_sorted.head(10)[["nome", "gc"]])
print("10 menores concentração CG:")
print(df_sorted.tail(10)[["nome", "gc"]])

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

# cria a coluna "seq_inicio" aplicando a função encontrar_inicio em cada sequência da coluna "sequencia"
df["seq_inicio"] = df["sequencia"].apply(encontrar_inicio) 
# cria a coluna "proteina" aplicando a função traduzir no resultado de encontrar_inicio para cada sequência
df["proteina"] = df["sequencia"].apply(lambda seq: traduzir(encontrar_inicio(seq), parar=True)) 
df["tamanho_proteina"] = df["proteina"].apply(len) # cria a coluna "tamanho_proteina" aplicando a função len na coluna "proteina"
df["cobertura"] = (df["tamanho_proteina"] * 3) / df["tamanho"] # cria a coluna "cobertura" calculando a cobertura com base no tamanho da proteína e da sequência


cobertura_mediana = df["cobertura"].median() # calcula a mediana da coluna "cobertura"
print("\n--- Conclusão sobre a proteína ---")
print(f"A cobertura média da poliproteína viral é de {cobertura_mediana:.2f}")
print("Indicando que a maior parte do genoma codifica uma única proteína longa.")

# Vírus com cobertura < 0.3 (quantos são?)
baixa_cobertura = df[df["cobertura"] < 0.3][["nome", "cobertura", "tamanho"]]
print(f"\nVírus com cobertura < 0.3 ({len(baixa_cobertura)} ocorrências):")
print(baixa_cobertura)

# Vírus com cobertura > 0.99 (quantos são?)
alta_cobertura = df[df["cobertura"] > 0.9][["nome", "cobertura", "tamanho"]]
print(f"\nVírus com cobertura > 0.9 ({len(alta_cobertura)} ocorrências):")
print(alta_cobertura)  

print("\n--- Conclusão sobre a cobertura ---")
print("A cobertura da poliproteína viral é tipicamente alta, próxima de 1")
print("Indicando que a maior parte do genoma é traduzida em uma única proteína longa.")

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

