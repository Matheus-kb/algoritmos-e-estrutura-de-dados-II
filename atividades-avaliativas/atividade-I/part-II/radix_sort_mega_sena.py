import csv
import os


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    if not arr:
        return arr

    max_num = max(arr)

    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr


def criar_chave_ordenacao(numeros):
    numeros_ordenados = sorted(numeros)
    chave = 0
    for i, num in enumerate(numeros_ordenados):
        chave += num * (100 ** (5 - i))
    return chave


def processar_mega_sena():
    arquivo_entrada = ".\draw-data\Mega-Sena-Resultados-Randomizados.csv"
    arquivo_saida = ".\draw-data\Mega-Sena-Resultados-Ordenados-RadixSort.csv"

    dados_sorteios = []

    print("Lendo arquivo de dados da Mega Sena...")

    try:
        with open(arquivo_entrada, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

            print(f"Cabeçalho: {linhas[0].strip()}")

            for i, linha in enumerate(linhas[1:], 1):
                try:
                    campos = linha.strip().split(";")

                    if len(campos) < 8:
                        print(f"Linha {i} com poucos campos: {len(campos)}")
                        continue

                    concurso = int(campos[0].strip())

                    numeros = [
                        int(campos[2].strip()),
                        int(campos[3].strip()),
                        int(campos[4].strip()),
                        int(campos[5].strip()),
                        int(campos[6].strip()),
                        int(campos[7].strip()),
                    ]

                    chave_ordenacao = criar_chave_ordenacao(numeros)

                    dados_sorteios.append(
                        {
                            "concurso": concurso,
                            "numeros": sorted(numeros),
                            "chave_ordenacao": chave_ordenacao,
                        }
                    )

                except (ValueError, IndexError) as e:
                    print(f"Erro ao processar linha {i}: {e}")
                    if i <= 5:
                        print(f"Dados da linha: {linha.strip()}")
                    continue

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {arquivo_entrada}")
        return
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return

    print(f"Total de sorteios carregados: {len(dados_sorteios)}")

    print("Aplicando Radix Sort...")
    chaves = [sorteio["chave_ordenacao"] for sorteio in dados_sorteios]
    indices_originais = list(range(len(chaves)))

    pares_chave_indice = list(zip(chaves, indices_originais))

    chaves_ordenadas = chaves.copy()
    radix_sort(chaves_ordenadas)

    dados_ordenados = []
    for chave_ordenada in chaves_ordenadas:
        for i, (chave_original, indice_original) in enumerate(pares_chave_indice):
            if chave_original == chave_ordenada:
                dados_ordenados.append(dados_sorteios[indice_original])
                pares_chave_indice.pop(i)
                break

    print("Salvando resultados ordenados...")

    try:
        with open(arquivo_saida, "w", encoding="utf-8", newline="") as arquivo:
            arquivo.write("Números Sorteados,Sorteio\n")

            for sorteio in dados_ordenados:
                numeros_formatados = (
                    "[" + ",".join([f"{num:02d}" for num in sorteio["numeros"]]) + "]"
                )
                arquivo.write(f"{numeros_formatados},{sorteio['concurso']}\n")

        print(f"Arquivo salvo com sucesso: {arquivo_saida}")

        print("\nPrimeiros 10 resultados ordenados:")
        print("Números Sorteados - Sorteio")
        for i in range(min(10, len(dados_ordenados))):
            sorteio = dados_ordenados[i]
            numeros_formatados = (
                "[" + ",".join([f"{num:02d}" for num in sorteio["numeros"]]) + "]"
            )
            print(f"{numeros_formatados} - {sorteio['concurso']}")

    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")


if __name__ == "__main__":
    print("=" * 60)
    print("ORDENAÇÃO DE RESULTADOS DA MEGA SENA USANDO RADIX SORT")
    print("=" * 60)
    processar_mega_sena()
    print("\nProcesso concluído!")
