# Randomizador de Resultados da Mega-Sena

Este script Python embaralha os dados do arquivo `Mega-Sena-Resultados-Ordenados.csv`, criando um novo arquivo com os mesmos dados em ordem aleatória.

## Funcionalidades

- ✅ Lê automaticamente o arquivo CSV com resultados ordenados
- ✅ Preserva o cabeçalho do arquivo original
- ✅ Embaralha todas as linhas de dados aleatoriamente
- ✅ Cria um novo arquivo com dados randomizados
- ✅ Detecta automaticamente o delimitador do CSV (ponto e vírgula)
- ✅ Exibe estatísticas do processamento
- ✅ Pergunta antes de sobrescrever arquivos existentes

## Como usar

1. Certifique-se de que o arquivo `Mega-Sena-Resultados-Ordenados.csv` está na mesma pasta do script
2. Execute o script:
   ```bash
   python randomizer.py
   ```
3. O arquivo `Mega-Sena-Resultados-Randomizados.csv` será criado com os dados embaralhados

## Arquivos

- **Entrada**: `Mega-Sena-Resultados-Ordenados.csv` (dados ordenados)
- **Saída**: `Mega-Sena-Resultados-Randomizados.csv` (dados embaralhados)

## Estrutura dos dados

O arquivo CSV contém informações sobre sorteios da Mega-Sena, incluindo:
- Número do concurso
- Data do sorteio
- Números sorteados (6 bolas)
- Informações sobre ganhadores e premiação
- Valores de arrecadação

## Exemplo de saída

```
=== RANDOMIZADOR DE RESULTADOS DA MEGA-SENA ===
Arquivo de entrada: Mega-Sena-Resultados-Ordenados.csv
Arquivo de saída: Mega-Sena-Resultados-Randomizados.csv
--------------------------------------------------
Arquivo lido com sucesso!
Total de registros (excluindo cabeçalho): 2920
Dados embaralhados com sucesso!
Arquivo 'Mega-Sena-Resultados-Randomizados.csv' criado com sucesso!
Os dados foram embaralhados e salvos em ordem aleatória.

✅ Randomização concluída com sucesso!
```

## Requisitos

- Python 3.x
- Módulos padrão: `csv`, `random`, `os` (já inclusos no Python)

## Observações

- O script usa uma seed aleatória diferente a cada execução
- Os dados originais não são modificados
- O cabeçalho do CSV é preservado na primeira linha
- Funciona com qualquer arquivo CSV que use ponto e vírgula como delimitador