import csv
import random
import os


def randomize_mega_sena_results(input_file, output_file):
    try:
        if not os.path.exists(input_file):
            print(f"Erro: Arquivo '{input_file}' não encontrado!")
            return False
        
        with open(input_file, 'r', encoding='utf-8') as file:
            sample = file.read(1024)
            file.seek(0)
            sniffer = csv.Sniffer()
            delimiter = sniffer.sniff(sample).delimiter
            
            reader = csv.reader(file, delimiter=delimiter)
            
            header = next(reader)
            
            data_rows = list(reader)
        
        print("Arquivo lido com sucesso!")
        print(f"Total de registros (excluindo cabeçalho): {len(data_rows)}")
        
        random.shuffle(data_rows)
        print("Dados embaralhados com sucesso!")
        
        with open(output_file, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=delimiter)
            
            writer.writerow(header)
            
            writer.writerows(data_rows)
        
        print(f"Arquivo '{output_file}' criado com sucesso!")
        print("Os dados foram embaralhados e salvos em ordem aleatória.")
        
        return True
        
    except Exception as e:
        print(f"Erro ao processar os arquivos: {e}")
        return False


def main():
    print("=== RANDOMIZADOR DE RESULTADOS DA MEGA-SENA ===")
    
    input_file = "./draw-data/Mega-Sena-Resultados-Ordenados.csv"
    output_file = "./draw-data/Mega-Sena-Resultados-Randomizados.csv"
    
    print(f"Arquivo de entrada: {input_file}")
    print(f"Arquivo de saída: {output_file}")
    print("-" * 50)
    
    if os.path.exists(output_file):
        response = input(f"O arquivo '{output_file}' já existe. Deseja sobrescrever? (s/n): ").lower().strip()
        if response not in ['s', 'sim', 'y', 'yes']:
            print("Operação cancelada pelo usuário.")
            return
    
    success = randomize_mega_sena_results(input_file, output_file)
    
    if success:
        print("\n✅ Randomização concluída com sucesso!")
        
        print("\n=== ESTATÍSTICAS ===")
        try:
            with open(output_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                print(f"Total de linhas no arquivo de saída: {len(lines)}")
                print(f"Primeira linha de dados (após cabeçalho): {lines[1].strip()}")
                print(f"Última linha de dados: {lines[-1].strip()}")
        except Exception as e:
            print(f"Erro ao ler estatísticas: {e}")
    else:
        print("\n❌ Falha na randomização!")


if __name__ == "__main__":
    random.seed()
    main()
