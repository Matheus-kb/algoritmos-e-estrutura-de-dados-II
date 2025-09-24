# Sistema de Ordenação de Pedidos com Quick Sort

Este projeto implementa um sistema para ordenar pedidos usando o algoritmo Quick Sort. Cada pedido possui um ID, valor monetário e horário de saída.

## Arquivos do Projeto

1. **quick-sort.py** - Implementação principal com exemplo fixo
2. **exemplo_pedidos_interativo.py** - Versão interativa com menu
3. **README.md** - Esta documentação

## Classe Pedido

A classe `Pedido` representa um pedido com as seguintes propriedades:

```python
class Pedido:
    def __init__(self, id, valor, horario_saida):
        self.id = id                    # Identificador único
        self.valor = valor              # Valor em reais (float)
        self.horario_saida = horario    # Objeto datetime
```

## Função de Ordenação

A função `quicksort_pedidos()` implementa o algoritmo Quick Sort para pedidos:

```python
def quicksort_pedidos(arr, criterio='valor'):
    """
    Ordena uma lista de pedidos usando Quick Sort
    criterio: 'valor' para ordenar por valor, 'horario' para ordenar por horário
    """
```

### Critérios de Ordenação

- **'valor'**: Ordena pelos valores dos pedidos (menor para maior)
- **'horario'**: Ordena pelos horários de saída (mais cedo para mais tarde)

## Como Usar

### Exemplo Básico

```python
from datetime import datetime

# Criar pedidos
pedidos = [
    Pedido(1, 45.80, datetime.strptime("14:30", "%H:%M")),
    Pedido(2, 23.50, datetime.strptime("12:15", "%H:%M")),
    Pedido(3, 67.20, datetime.strptime("13:45", "%H:%M"))
]

# Ordenar por valor
pedidos_por_valor = quicksort_pedidos(pedidos, 'valor')

# Ordenar por horário
pedidos_por_horario = quicksort_pedidos(pedidos, 'horario')
```

### Executar os Exemplos

1. **Exemplo fixo**:
   ```bash
   python quick-sort.py
   ```

2. **Exemplo interativo**:
   ```bash
   python exemplo_pedidos_interativo.py
   ```

## Complexidade do Algoritmo

- **Melhor caso**: O(n log n)
- **Caso médio**: O(n log n)
- **Pior caso**: O(n²)
- **Espaço**: O(log n) devido à recursão

## Características do Quick Sort

1. **Algoritmo de divisão e conquista**
2. **Ordenação in-place** (versão otimizada)
3. **Não estável** (pode alterar a ordem relativa de elementos iguais)
4. **Eficiente na prática** para a maioria dos casos

## Exemplo de Saída

```
=== ORDENAÇÃO DE PEDIDOS ===
Lista original de pedidos:
  Pedido 1: R$45.80 - Saída: 14:30
  Pedido 2: R$23.50 - Saída: 12:15
  Pedido 3: R$67.20 - Saída: 13:45

--- Ordenação por VALOR (crescente) ---
  Pedido 2: R$23.50 - Saída: 12:15
  Pedido 1: R$45.80 - Saída: 14:30
  Pedido 3: R$67.20 - Saída: 13:45

--- Ordenação por HORÁRIO DE SAÍDA (crescente) ---
  Pedido 2: R$23.50 - Saída: 12:15
  Pedido 3: R$67.20 - Saída: 13:45
  Pedido 1: R$45.80 - Saída: 14:30
```

## Possíveis Extensões

1. **Ordenação decrescente**: Inverter as comparações
2. **Múltiplos critérios**: Ordenar por valor e depois por horário
3. **Interface gráfica**: Criar uma GUI para visualizar a ordenação
4. **Análise de performance**: Comparar com outros algoritmos
5. **Persistência**: Salvar/carregar pedidos de arquivos