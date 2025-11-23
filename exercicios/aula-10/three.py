class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = []

    def adicionar_filho(self, filho):
        self.proximo.append(filho)


class Arvore:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def adicionar_no(self, valor, pai=None):
        novo_no = No(valor)
        if pai is None:
            if self.raiz is None:
                self.raiz = novo_no
            else:
                self.raiz.adicionar_filho(novo_no)
        else:
            pai.adicionar_filho(novo_no)
        return novo_no

    def vazia(self):
        return self.raiz is None

    def buscar_no(self, valor, no_atual=None):
        if no_atual is None:
            no_atual = self.raiz
        
        if no_atual is None:
            return None
        
        if no_atual.valor == valor:
            return no_atual
        
        for filho in no_atual.proximo:
            resultado = self.buscar_no(valor, filho)
            if resultado is not None:
                return resultado
        
        return None

    def imprimir(self, no_atual=None, nivel=0):
        if no_atual is None:
            no_atual = self.raiz
        
        if no_atual is None:
            print("Árvore vazia")
            return
        
        print("  " * nivel + str(no_atual.valor))
        for filho in no_atual.proximo:
            self.imprimir(filho, nivel + 1)

    def adicionar_ramo(self):
        while True:
            self.imprimir()
            print("\nEntre com os dados ou ENTER para encerrar")
            valor = input("Valor do nó: ")
            if not valor:
                break
            
            pai_no = None
            if not self.vazia():
                pai_valor = input("Valor do nó pai (ou ENTER para raiz): ")
                if pai_valor:
                    pai_no = self.buscar_no(pai_valor)
                    if pai_no is None:
                        print(f"Nó pai '{pai_valor}' não encontrado!")
                        continue
            
            self.adicionar_no(valor, pai_no)

arvore = Arvore()
arvore.adicionar_ramo()
