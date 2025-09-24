from datetime import datetime
import random

class Pedido:
    def __init__(self, id, valor, horario_saida):
        self.id = id
        self.valor = valor
        self.horario_saida = horario_saida
    
    def __str__(self):
        return f"Pedido {self.id}: R${self.valor:.2f} - Saída: {self.horario_saida.strftime('%H:%M')}"
    
    def __repr__(self):
        return self.__str__()

def quicksort_pedidos(arr, criterio='valor'):
    """
    Ordena uma lista de pedidos usando Quick Sort
    criterio: 'valor' para ordenar por valor, 'horario' para ordenar por horário
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        
        if criterio == 'valor':
            left = [x for x in arr[1:] if x.valor <= pivot.valor]
            right = [x for x in arr[1:] if x.valor > pivot.valor]
        elif criterio == 'horario':
            left = [x for x in arr[1:] if x.horario_saida <= pivot.horario_saida]
            right = [x for x in arr[1:] if x.horario_saida > pivot.horario_saida]
        else:
            raise ValueError("Critério deve ser 'valor' ou 'horario'")
        
        return quicksort_pedidos(left, criterio) + [pivot] + quicksort_pedidos(right, criterio)

def gerar_pedidos_aleatorios(quantidade=10):
    """Gera uma lista de pedidos com valores e horários aleatórios"""
    pedidos = []
    
    for i in range(1, quantidade + 1):
        # Gerar valor aleatório entre R$ 10,00 e R$ 150,00
        valor = round(random.uniform(10.0, 150.0), 2)
        
        # Gerar horário aleatório entre 10:00 e 18:00
        hora = random.randint(10, 17)
        minuto = random.choice([0, 15, 30, 45])
        horario = datetime.strptime(f"{hora:02d}:{minuto:02d}", "%H:%M")
        
        pedidos.append(Pedido(i, valor, horario))
    
    return pedidos

def exibir_lista(pedidos, titulo):
    """Exibe uma lista de pedidos formatada"""
    print(f"\n{titulo}")
    print("-" * len(titulo))
    for i, pedido in enumerate(pedidos, 1):
        print(f"{i:2d}. {pedido}")

def main():
    print("=== SISTEMA DE ORDENAÇÃO DE PEDIDOS ===")
    print("Usando algoritmo Quick Sort")
    
    # Gerar pedidos aleatórios
    print("\nGerando 12 pedidos aleatórios...")
    pedidos = gerar_pedidos_aleatorios(12)
    
    # Exibir lista original
    exibir_lista(pedidos, "LISTA ORIGINAL (desordenada)")
    
    # Menu de opções
    while True:
        print("\n" + "="*50)
        print("OPÇÕES DE ORDENAÇÃO:")
        print("1. Ordenar por VALOR (menor para maior)")
        print("2. Ordenar por HORÁRIO DE SAÍDA (mais cedo para mais tarde)")
        print("3. Gerar nova lista aleatória")
        print("4. Sair")
        
        try:
            opcao = input("\nEscolha uma opção (1-4): ").strip()
            
            if opcao == '1':
                pedidos_ordenados = quicksort_pedidos(pedidos.copy(), 'valor')
                exibir_lista(pedidos_ordenados, "PEDIDOS ORDENADOS POR VALOR")
                
            elif opcao == '2':
                pedidos_ordenados = quicksort_pedidos(pedidos.copy(), 'horario')
                exibir_lista(pedidos_ordenados, "PEDIDOS ORDENADOS POR HORÁRIO DE SAÍDA")
                
            elif opcao == '3':
                pedidos = gerar_pedidos_aleatorios(12)
                exibir_lista(pedidos, "NOVA LISTA GERADA (desordenada)")
                
            elif opcao == '4':
                print("\nPrograma encerrado!")
                break
                
            else:
                print("Opção inválida! Tente novamente.")
                
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário!")
            break
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()