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

    def remover_no(self, valor):
        # Método público para remover um nó da árvore
        # Verifica se a árvore está vazia antes de tentar remover
        if self.vazia():
            print("Árvore vazia, nada para remover")
            return
        
        print(f"----- Removendo Nó: {valor} ------")
        self.raiz = self._remover_no(self.raiz, valor)

    def _remover_no(self, no_atual, valor):
        # Método privado recursivo para remover um nó
        input(f">>> NoAtual: {str(no_atual)}")
        
        # Passo 1: Realizar remoção BST padrão
        if not no_atual:
            print("    Valor não encontrado na árvore")
            return no_atual
        
        # Navegar pela árvore para encontrar o nó a ser removido
        if valor < no_atual.valor:
            # Valor está na subárvore esquerda
            no_atual.esquerda = self._remover_no(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            # Valor está na subárvore direita
            no_atual.direita = self._remover_no(no_atual.direita, valor)
        else:
            # Nó encontrado! Realizar remoção
            print(f"    Nó encontrado: {valor}")
            
            # Caso 1: Nó com apenas um filho ou nenhum filho
            if no_atual.esquerda is None:
                print("    Nó tem apenas filho direito (ou nenhum)")
                temp = no_atual.direita
                no_atual = None
                return temp
            elif no_atual.direita is None:
                print("    Nó tem apenas filho esquerdo")
                temp = no_atual.esquerda
                no_atual = None
                return temp
            
            # Caso 2: Nó com dois filhos
            # Encontrar o sucessor in-order (menor valor na subárvore direita)
            print("    Nó tem dois filhos, buscando sucessor")
            temp = self._no_minimo(no_atual.direita)
            print(f"    Sucessor encontrado: {temp.valor}")
            
            # Copiar o valor do sucessor para este nó
            no_atual.valor = temp.valor
            
            # Remover o sucessor
            no_atual.direita = self._remover_no(no_atual.direita, temp.valor)
        
        # Se a árvore tinha apenas um nó, retornar
        if no_atual is None:
            return no_atual
        
        # Passo 2: Atualizar altura do nó atual
        no_atual.altura = 1 + max(
            self._altura(no_atual.esquerda),
            self._altura(no_atual.direita)
        )
        
        input(f"    NoAtual {str(no_atual.valor)}  Altura: {no_atual.altura}")
        
        # Passo 3: Calcular fator de balanceamento
        balanceamento = self._balanceamento(no_atual)
        
        input(f"   FB: {str(balanceamento)}")
        
        # Passo 4: Rebalancear a árvore se necessário
        
        # Caso Esquerda-Esquerda (FB < -1 e filho esquerdo está desbalanceado à esquerda)
        if balanceamento < -1 and self._balanceamento(no_atual.esquerda) <= 0:
            input("Fazer Rotação a Direita (Caso EE)")
            return self._rotacao_direita(no_atual)
        
        # Caso Esquerda-Direita (FB < -1 e filho esquerdo está desbalanceado à direita)
        if balanceamento < -1 and self._balanceamento(no_atual.esquerda) > 0:
            input("Fazer Rotação Dupla: Esquerda-Direita (Caso ED)")
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)
        
        # Caso Direita-Direita (FB > 1 e filho direito está desbalanceado à direita)
        if balanceamento > 1 and self._balanceamento(no_atual.direita) >= 0:
            input("Fazer Rotação a Esquerda (Caso DD)")
            return self._rotacao_esquerda(no_atual)
        
        # Caso Direita-Esquerda (FB > 1 e filho direito está desbalanceado à esquerda)
        if balanceamento > 1 and self._balanceamento(no_atual.direita) < 0:
            input("Fazer Rotação Dupla: Direita-Esquerda (Caso DE)")
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)
        
        return no_atual

    def _no_minimo(self, no):
        # Método auxiliar para encontrar o nó com menor valor
        # (usado para encontrar o sucessor in-order)
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

#################################

def popular_arvore(arvore):
    lista_entradas = [100, 50, 20, 80, 90, 85] #[100, 50, 80, 200, 300, 60, 90, 250, 55]
    for e in lista_entradas:
        arvore.imprimir()
        arvore.adicionar_no(e)

    print("\nÁrvore completa")
    arvore.imprimir()

def testar_remocao(arvore):
    # Testando remoção de diferentes nós
    valores_para_remover = [20, 50, 100]
    
    for valor in valores_para_remover:
        print(f"\n{'='*50}")
        print(f"Removendo o valor: {valor}")
        print('='*50)
        arvore.remover_no(valor)
        arvore.imprimir()


# Criando uma árvore
arvore = ArvoreAVL()

# Adicionando nós na árvore
#adicionar_ramo(arvore)
popular_arvore(arvore)

# Testando remoção (descomente para testar)
testar_remocao(arvore)


