from datetime import datetime

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


pedidos = [
    Pedido(1, 45.80, datetime.strptime("14:30", "%H:%M")),
    Pedido(2, 23.50, datetime.strptime("12:15", "%H:%M")),
    Pedido(3, 67.20, datetime.strptime("13:45", "%H:%M")),
    Pedido(4, 12.90, datetime.strptime("11:30", "%H:%M")),
]

print("=== ORDENAÇÃO DE PEDIDOS ===")
print("Lista original de pedidos:")
for pedido in pedidos:
    print(f"  {pedido}")

print("\n--- Ordenação por VALOR (crescente) ---")
pedidos_por_valor = quicksort_pedidos(pedidos.copy(), 'valor')
for pedido in pedidos_por_valor:
    print(f"  {pedido}")

print("\n--- Ordenação por HORÁRIO DE SAÍDA (crescente) ---")
pedidos_por_horario = quicksort_pedidos(pedidos.copy(), 'horario')
for pedido in pedidos_por_horario:
    print(f"  {pedido}")
