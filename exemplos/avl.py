class No:
    def __init__(self, valor):
        self.esquerda = None
        self.valor = valor
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def vazia(self):
        if self.raiz is None:
            return True
        return False

    def adicionar_no(self, valor):
        if self.vazia():
            novo_No = No(valor) ###
            input( f"Primeiro No: {str(novo_No)[-5:]} "
                   f"-- Valor: {str(novo_No.valor)}  Altura: {str(novo_No.altura)}  "
                   f"Esq.{str(novo_No.esquerda)[-5:]}  Dir.{str(novo_No.direita)[-5:]}\nEnter")
            self.raiz = novo_No
        else:
            print(f"----- Adicionando Nó Folha: {valor} ------")
            self.raiz = self._adicionar_no_folha(self.raiz, valor)

    def _adicionar_no_folha(self, no_atual, valor):
        input(f">>> NoAtual: {str(no_atual)}")
        if not no_atual:
            novo_No = No(valor) ###
            print( f"    NovoNo: {str(novo_No)[-5:]} "
                   f"-- Esq.{str(novo_No.esquerda)[-5:]} Valor: {str(novo_No.valor)}  Dir.{str(novo_No.direita)[-5:]}"
                   f"   Altura {str(novo_No.altura)}")
            return novo_No
        elif valor < no_atual.valor:
            no_atual.esquerda = self._adicionar_no_folha(no_atual.esquerda, valor)
        else:
            no_atual.direita = self._adicionar_no_folha(no_atual.direita, valor)

        ############################# altura
        no_atual.altura = 1 + max(
            self._altura(no_atual.esquerda),
            self._altura(no_atual.direita)
        )

        input(f"    NoAtual {str(no_atual.valor)}  Altura: {no_atual.altura}")

        ############################# Fator Balanceamento
        balanceamento = self._balanceamento(no_atual)

        input(f"   FB: {str(balanceamento)}")

        if balanceamento < -1:
            if valor < no_atual.esquerda.valor:
                input("Fazer Rotação a Direita +")
                return self._rotacao_direita(no_atual)
            else:
                input("Fazer Rotação a Esquerda +")
                no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
                return self._rotacao_direita(no_atual)

        if balanceamento > 1:
            if valor > no_atual.direita.valor:
                input("Fazer Rotação a Direita em -")
                return self._rotacao_esquerda(no_atual)
            else:
                input("Fazer Rotação a Esquerda em -")
                no_atual.direita = self._rotacao_direita(no_atual.direita)
                return self._rotacao_esquerda(no_atual)

        return no_atual

    def _altura(self, no):
        if not no:
            return 0
        return no.altura

    def _balanceamento(self, no):
        if not no:
            return 0
        fb = self._altura(no.direita) - self._altura(no.esquerda)
        return fb

    def _rotacao_esquerda(self, pai):
        filhoD = pai.direita
        neto = filhoD.esquerda

        print("Antes da Rotacao Esquerda")
        print(
            f"   : {str(pai)[-5:]} -- Esq.{str(pai.esquerda)[-5:]} Valor: {str(pai.valor)}  Dir.{str(pai.direita)[-5:]}")
        print(
            f"   : {str(filhoD)[-5:]} -- Esq.{str(filhoD.esquerda)[-5:]} Valor: {str(filhoD.valor)}  Dir.{str(filhoD.direita)[-5:]}")

        filhoD.esquerda = pai
        pai.direita = neto

        print("Apos da Rotacao Esquerda")
        print(
            f"   : {str(pai)[-5:]} -- Esq.{str(pai.esquerda)[-5:]} Valor: {str(pai.valor)}  Dir.{str(pai.direita)[-5:]}")
        print(
            f"   : {str(filhoD)[-5:]} -- Esq.{str(filhoD.esquerda)[-5:]} Valor: {str(filhoD.valor)}  Dir.{str(filhoD.direita)[-5:]}")

        pai.altura = 1 + max(
            self._altura(pai.esquerda),
            self._altura(pai.direita))
        filhoD.altura = 1 + max(
            self._altura(filhoD.esquerda),
            self._altura(filhoD.direita))

        input("Enter")

        return filhoD

    def _rotacao_direita(self, pai):
        filhoE = pai.esquerda
        neto = filhoE.direita

        print("Antes da Rotacao Direita")
        print(
            f"    : {str(pai)[-5:]} -- Esq.{str(pai.esquerda)[-5:]} Valor: {str(pai.valor)}  Dir.{str(pai.direita)[-5:]}")
        print(
            f"    : {str(filhoE)[-5:]} -- Esq.{str(filhoE.esquerda)[-5:]} Valor: {str(filhoE.valor)}  Dir.{str(filhoE.direita)[-5:]}")

        filhoE.direita = pai
        pai.esquerda = neto

        print("Após da Rotacao Direita")
        print(
            f"    : {str(pai)[-5:]} -- Esq.{str(pai.esquerda)[-5:]} Valor: {str(pai.valor)}  Dir.{str(pai.direita)[-5:]}")
        print(
            f"    : {str(filhoE)[-5:]} -- Esq.{str(filhoE.esquerda)[-5:]} Valor: {str(filhoE.valor)}  Dir.{str(filhoE.direita)[-5:]}")

        pai.altura = 1 + max(
            self._altura(pai.esquerda),
            self._altura(pai.direita))
        filhoE.altura = 1 + max(
            self._altura(filhoE.esquerda),
            self._altura(filhoE.direita))
        input("Enter")
        return filhoE

    def imprimir(self):
        if self.vazia():
            print("========== Árvore vazia ==========")
            return
        print("\n=============== Árvore ================")
        self._imprimir(self.raiz)
        print("=========================================\n")

    def _imprimir(self, no_atual):
        if no_atual is not None:
            self._imprimir(no_atual.esquerda)
            print(f"Nó: {str(no_atual)[-5:]} -- Esq.{str(no_atual.esquerda)[-5:]} Valor: {str(no_atual.valor)}  Dir.{str(no_atual.direita)[-5:]} Alt.{str(no_atual.altura)}")
            self._imprimir(no_atual.direita)

#################################

def popular_arvore(arvore):
    lista_entradas = [100, 50, 20, 80, 90, 85] #[100, 50, 80, 200, 300, 60, 90, 250, 55]
    for e in lista_entradas:
        arvore.imprimir()
        arvore.adicionar_no(e)

    print("\nÁrvore completa")
    arvore.imprimir()




# Criando uma árvore
arvore = ArvoreAVL()

# Adicionando nós na árvore
#adicionar_ramo(arvore)
popular_arvore(arvore)


