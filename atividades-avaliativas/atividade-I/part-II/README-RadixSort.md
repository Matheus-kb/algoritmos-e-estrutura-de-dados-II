# Ordenação de Números da Mega Sena usando Radix Sort

## Descrição do Projeto

Este projeto implementa um algoritmo de ordenação **Radix Sort** para organizar os números sorteados da Mega Sena em ordem crescente. O objetivo é processar um arquivo CSV com resultados randomizados da Mega Sena e gerar um arquivo ordenado no formato solicitado.

## Algoritmo Implementado: Radix Sort

### O que é o Radix Sort?

O **Radix Sort** é um algoritmo de ordenação não-comparativo que ordena números inteiros processando dígito por dígito, da posição menos significativa (unidades) para a mais significativa (centenas, milhares, etc.).

### Características do Radix Sort:

- **Complexidade de Tempo**: O(d × (n + k))
  - `d` = número de dígitos do maior número
  - `n` = número de elementos
  - `k` = range dos dígitos (0-9 para base decimal)
- **Complexidade de Espaço**: O(n + k)
- **Estabilidade**: Estável (mantém a ordem relativa de elementos iguais)
- **Tipo**: Algoritmo não-comparativo

### Vantagens:
- Muito eficiente para ordenar grandes quantidades de números inteiros
- Complexidade linear em muitos casos práticos
- Algoritmo estável

### Como funciona no projeto:
1. Cada conjunto de 6 números da Mega Sena é convertido em uma chave única
2. O Radix Sort ordena essas chaves processando dígito por dígito
3. Os sorteios são reordenados baseados nas chaves ordenadas

## Estrutura do Projeto

```
atividades-avaliativas/atividade-I/part-II/
├── draw-data/
│   ├── Mega-Sena-Resultados-Randomizados.csv      # Arquivo de entrada
│   └── Mega-Sena-Resultados-Ordenados-RadixSort.csv # Arquivo de saída
└── radix_sort_mega_sena.py                        # Script principal
```

## Arquivo Principal

### `radix_sort_mega_sena.py`
Script que implementa a ordenação dos números da Mega Sena usando Radix Sort:
- Implementação completa do algoritmo Radix Sort
- Função auxiliar Counting Sort
- Processamento de arquivo CSV
- Geração de chave única para ordenação
- Saída formatada conforme solicitado

## Como usar

### Pré-requisitos
- Python 3.x instalado
- Arquivo `Mega-Sena-Resultados-Randomizados.csv` na pasta `draw-data/`

### Execução
```bash
# Navegar para o diretório do projeto
cd "\algoritimos-II\atividades-avaliativas\atividade-I\part-II"

# Executar o script
python radix_sort_mega_sena.py
```

## Formato dos Dados

### Entrada (CSV)
```
Concurso;Data do Sorteio;Bola1;Bola2;Bola3;Bola4;Bola5;Bola6;...
2918;23/09/2025;11;27;31;41;48;54;...
1997;16/12/2017;1;7;14;31;35;46;...
```

### Saída (CSV)
```
Números Sorteados,Sorteio
[01,02,03,11,28,43],1474
[01,02,05,24,32,46],397
[01,02,06,09,16,32],1505
```

## Resultados

O script processa **2.920 sorteios** da Mega Sena e os ordena com base nos números sorteados em ordem crescente. 

### Exemplos de saída:
- **Primeiro resultado**: `[01,02,03,11,28,43] - 1474`
- **Último resultado**: `[50,51,56,57,58,59] - 2052`

## Funcionalidades Implementadas

1. **Leitura de CSV**: Processa o arquivo de entrada com tratamento de erros
2. **Radix Sort**: Implementação completa do algoritmo
3. **Chave de Ordenação**: Converte conjuntos de números em chaves únicas
4. **Formatação**: Saída no formato solicitado `[XX,XX,XX,XX,XX,XX] - XXXX`
5. **Relatórios**: Exibe estatísticas e exemplos dos resultados

## Considerações Técnicas

- **Encoding**: UTF-8 para compatibilidade com caracteres especiais
- **Separador CSV**: Ponto e vírgula (;) para entrada, vírgula (,) para saída
- **Formato de Números**: Números com zero à esquerda (01, 02, etc.)
- **Tratamento de Erros**: Ignora linhas malformadas e continua o processamento

## Autor

Trabalho desenvolvido para a disciplina de **Algoritmos e Estrutura de Dados II**.
Data: Setembro 2025