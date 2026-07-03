# Projeto - Escrevendo nossa própria "BioPython"

Para treinar o que aprendemos durante o curso, vamos criar algumas funções inspiradas na
biblioteca BioPython. E vamos usá-las para resolver alguns problemas de Bioinformática.

Vai ser algo simplificado, apenas com o intuito de treinarmos as ferramentas que vimos em
sala de aula: strings, listas, dicionários, funções e, no final, **pandas**.

--------------------------

## Preparando o ambiente

O último problema usa a biblioteca **pandas**. Para instalá-la, rode no terminal:

```
pip install -r requirements.txt
```

--------------------------

## Como os dados são representados

Nada de classes por aqui! Vamos usar só o que já conhecemos:

- Uma **sequência** de DNA é uma **string**. Ex: `"ATCG"`.
- Um **organismo** (uma entrada do arquivo FASTA) é um **dicionário** com três chaves:
  `{"id": "NC_074786.1", "nome": "Guereza hepacivirus...", "sequencia": "CACTCC..."}`.
- Um **arquivo FASTA inteiro** vira uma **lista de dicionários** (um dicionário por organismo).

Esse formato é bem prático: dá para percorrer com um `for`, e no exercício de pandas ele
vira uma tabela com uma linha por organismo.

--------------------------

## Já está pronto para você (código de apoio)

### Função `ler_fasta(caminho_do_arquivo)`  —  em `bio/ler_fasta.py`

Inspirada na `SeqIO.parse`. **Você não precisa escrever esta função**, ela já está pronta.
Ela lê um arquivo FASTA e devolve a **lista de dicionários** descrita acima.

```python
from bio.ler_fasta import ler_fasta

organismos = ler_fasta("arquivos/Flaviviridae-genomes.fasta")
print(organismos[0]["nome"])        # nome do primeiro organismo
print(organismos[0]["sequencia"])   # sequência (string) do primeiro organismo
```

### Constantes  —  em `bio/constantes.py`

- `DNA_PARA_AMINOACIDO`: dicionário que traduz cada códon (trinca) no seu aminoácido.
- `DNA_STOP_CODONS`: lista com os códons de parada (stop codons).

--------------------------

## Para ser criado por você

Todas estas funções ficam em `bio/sequencia.py` (já com o esqueleto e dicas). Cada uma
recebe a sequência como uma **string** e devolve um resultado.

- `complementar(sequencia)` — inspirado no `Seq().complement()`
  - Retorna a string da sequência complementar (A<->T, C<->G).
  - Ex: `complementar("ATCG")` -> `"TAGC"`

- `complementar_reversa(sequencia)` — inspirado no `Seq().reverse_complement()`
  - Retorna a string da sequência complementar reversa.
  - Ex: `complementar_reversa("ATCG")` -> `"CGAT"`

- `transcrever(sequencia)` — inspirado no `Seq().transcribe()`
  - Retorna a string resultante da transcrição (DNA -> RNA; o T vira U).
  - Ex: `transcrever("ATCG")` -> `"AUCG"`

- `traduzir(sequencia, parar=False)` — inspirado no `Seq().translate()`
  - Retorna uma string com a tradução da sequência para uma proteína.
  - Ex: `traduzir("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")` -> `"MAIVMGR*KGAR*"`
  - Leia a sequência de 3 em 3 (cada trinca é um códon) e use o dicionário
    `DNA_PARA_AMINOACIDO`. Stop codons viram `*`; trincas fora do dicionário (base
    indefinida) viram `X`.
  - Se `parar=True`, a tradução para no primeiro stop codon. Se `parar=False`, continua
    até o fim marcando os stops como `*`.

- `calcular_percentual(sequencia, bases)` — (inventada por nós)
  - Recebe uma lista de bases e retorna o percentual delas na sequência.
  - Ex: `calcular_percentual("ATCGAAA", ["A"])` -> `0.5`
  - Ex: `calcular_percentual("ATCGCC", ["C", "G"])` -> `~0.66`

- `contar_bases(sequencia)` — (inventada por nós)
  - Retorna um dicionário com a contagem de cada base.
  - Ex: `contar_bases("ATCGA")` -> `{"A": 2, "T": 1, "C": 1, "G": 1}`

- `encontrar_inicio(sequencia)` — (inventada por nós)
  - Retorna a sequência a partir do primeiro **start codon** (`ATG`), que é onde a tradução
    de um gene começa. Se não houver `ATG`, retorna uma string vazia `""`.
  - Ex: `encontrar_inicio("CCATGGGGTAA")` -> `"ATGGGGTAA"`
  - Usamos ela junto com `traduzir` para achar a proteína: `traduzir(encontrar_inicio(seq), parar=True)`.

----------------------

## Usando

Depois de criar suas funções, vamos usá-las numa investigação de verdade: montar uma tabela
(com pandas) descrevendo mais de 150 vírus da família Flaviviridae e tirar conclusões sobre
eles. O projeto está descrito na pasta `problemas` (arquivo `problemas/README.md`).

-----------------------

## Avaliação

Diferente das nossas tarefas de casa, não terá avaliação automática. Eu vou ler e avaliar
e dar uma nota com cuidado.

Então mesmo se não funcionar 100%, eu vou conseguir dar nota de acordo com a solução.
