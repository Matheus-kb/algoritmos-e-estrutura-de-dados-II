class No:
    def __init__(self, valor):
        self.esquerda = None
        self.valor = valor
        self.direita = None

class Arvore:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def vazia(self):
        if self.raiz is None:
            return True
        return False

    def adicionar_no(self, valor):
        novo_no = No(valor)

        if self.vazia():
            self.raiz = novo_no
        else:
            self._adicionar_no_folha(novo_no, self.raiz)

    def _adicionar_no_folha(self, novo_no, no_atual):
        if novo_no.valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = novo_no
            else:
                self._adicionar_no_folha(novo_no, no_atual.esquerda)

        else:
            if no_atual.direita is None:
                no_atual.direita = novo_no
            else:
                self._adicionar_no_folha(novo_no, no_atual.direita)


    def imprimir(self):
        if self.vazia():
            print("----Árvore vazia----")
            return
        self._imprimir(self.raiz)

    # def _imprimir(self, no_atual):
    #     if no_atual is not None:
    #         self._imprimir(no_atual.esquerda)
    #         print(f" Valor:{str(no_atual.valor)} ")
    #         self._imprimir(no_atual.direita)

    def _imprimir(self, no_atual):
        if no_atual is not None:
            self._imprimir(no_atual.esquerda)
            print(f"Nó: {str(no_atual)[-5:-1]}>>> Esq.[{str(no_atual.esquerda)[-5:-1]}] --- Valor:{str(no_atual.valor)} --- Dir.[{str(no_atual.direita)[-5:-1]}]")
            self._imprimir(no_atual.direita)

    def buscar_no(self, no_atual, valor):
        if no_atual is not None:
            if no_atual.valor == valor:
                return no_atual

            no_encontrado =  self.buscar_no(no_atual.esquerda, valor)
            if no_encontrado:
                return no_encontrado
            return self.buscar_no(no_atual.direita, valor)



#
####################################################################
#
# Função para adicionar nós na árvore automaticamente
def popular_arvore(arvore):
    lista_entradas =[100, 50, 80, 200, 300, 60, 90, 250, 55]
    arvore.imprimir()
    for e in lista_entradas:
        arvore.adicionar_no(e)
    print("\nÁrvore completa")
    arvore.imprimir()

# Função para adicionar nós na árvore
def adicionar_ramo(arvore):
    while True:
        arvore.imprimir()

        print("\nEntre com os dados ou ENTER para encerrar!")
        valor = input("Digite o valor/dado a ser inserido: ")
        if not valor:
            break
        arvore.adicionar_no(int(valor))
    print("\nÁrvore completa")
    arvore.imprimir()


def procurar_arvore(numero):
    no_retorno = arvore.buscar_no(arvore.raiz, numero)
    if no_retorno:
        print(f"Achei o valor: {numero} no endereço: {str(no_retorno)[-5:-1]}")
    else:
        print(f"Valor: {numero} não consta na árvore.")


# Criando uma árvore
arvore = Arvore()

# Adicionando nós na árvore
# adicionar_ramo(arvore)
popular_arvore(arvore)



# Verificar se um valor existe na Árvore
procurar_arvore(255)