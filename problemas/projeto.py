# O Projeto: um panorama da família Flaviviridae
#
# ┌───────────────────────────────────────────────────────────────────────┐
# │  ATENÇÃO: rode este arquivo A PARTIR DA RAIZ do projeto, com -m:       │
# │      python -m problemas.projeto                                       │
# │  (com ponto e SEM ".py" no final; não é "python problemas/projeto.py") │
# │                                                                        │
# │  Rodar de outro jeito causa dois erros comuns:                        │
# │    - ModuleNotFoundError: No module named 'bio'                        │
# │    - FileNotFoundError: ...arquivos/Flaviviridae-genomes.fasta         │
# │  Os dois somem rodando com -m a partir da raiz, porque as pastas       │
# │  "bio" e "arquivos" ficam na raiz do projeto. Veja o README da raiz.   │
# └───────────────────────────────────────────────────────────────────────┘
#
# Leia o enunciado completo em problemas/README.md
#
# A ideia é construir UMA tabela (pandas) descrevendo os vírus e, a partir dela,
# tirar duas conclusões:
#   - o conteúdo GC é aleatório? (Parte 2)
#   - quão grande é a proteína de cada vírus? (Parte 3)
#
# Vá preenchendo as partes abaixo, uma de cada vez.

import pandas as pd

from bio.ler_fasta import ler_fasta
from bio.sequencia import (
    traduzir,
    calcular_percentual,
    encontrar_inicio,
)


# ------------------------------------------------------------------
# Parte 1 — Monte a tabela
# ------------------------------------------------------------------
organismos = ler_fasta("arquivos/Flaviviridae-genomes.fasta")
df = pd.DataFrame(organismos)
print(df.head())
# 3) crie a coluna "tamanho" (número de bases)


# ------------------------------------------------------------------
# Parte 2 — O conteúdo GC é aleatório?
# ------------------------------------------------------------------
# 1) crie a coluna "gc" com calcular_percentual(seq, ["G", "C"])
# 2) mostre os 10 maiores e os 10 menores GC (com o nome!)
# 3) escreva sua conclusão sobre o padrão que observou


# ------------------------------------------------------------------
# Parte 3 — Encontre a proteína (a poliproteína viral)
# ------------------------------------------------------------------
# 1) coluna "proteina": traduzir(encontrar_inicio(seq), parar=True)
# 2) coluna "tamanho_proteina": len da proteína
# 3) coluna "cobertura": (tamanho_proteina * 3) / tamanho
# 4) escreva sua conclusão (qual a cobertura típica? faz sentido ser 1 poliproteína?)


# ------------------------------------------------------------------
# Parte 4 — Salve o resultado
# ------------------------------------------------------------------
# 1) filtre os vírus com gc > 0.5 (quantos são?)
# 2) df.to_csv("resultado.csv", index=False)
