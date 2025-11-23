"""
Árvore AVL com Visualização Gráfica Simples
Versão otimizada e sem bugs
"""

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # Backend mais estável

class No:
    def __init__(self, valor):
        self.esquerda = None
        self.valor = valor
        self.direita = None
        self.altura = 1

class ArvoreAVLVisual:
    def __init__(self, raiz=None):
        self.raiz = raiz
        self.destaque_no = None
        self.mensagem = ""
        self.texto_mensagem = None  # Referência para o texto da mensagem
        # Criar figura uma única vez
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        plt.ion()  # Modo interativo

    def vazia(self):
        return self.raiz is None

    def visualizar(self, titulo="Árvore AVL"):
        """
        Desenha a árvore de forma simples e eficiente
        """
        self.ax.clear()  # Limpar apenas o eixo, não a figura
        ax = self.ax
        fig = self.fig
        
        # Remover mensagem anterior se existir
        if self.texto_mensagem:
            self.texto_mensagem.remove()
            self.texto_mensagem = None
        
        if self.vazia():
            ax.text(0.5, 0.5, 'Árvore Vazia', 
                   ha='center', va='center', fontsize=20, color='gray')
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
        else:
            # Desenhar árvore recursivamente
            self._desenhar_no(ax, self.raiz, 0, 0, 1.0)
        
        # Título
        ax.set_title(titulo, fontsize=16, fontweight='bold', pad=20)
        
        # Mensagem - armazenar referência
        if self.mensagem:
            self.texto_mensagem = fig.text(0.5, 0.02, self.mensagem, 
                    ha='center', fontsize=10,
                    bbox={'boxstyle': 'round', 'facecolor': 'yellow', 'alpha': 0.5})
        
        ax.axis('off')
        ax.set_aspect('equal')
        plt.tight_layout()
        plt.draw()
        plt.pause(0.01)  # Pausa mínima apenas para atualizar

    def _desenhar_no(self, ax, no, x, y, dx):
        """
        Desenha um nó e seus filhos recursivamente
        """
        if no is None:
            return
        
        # Calcular FB e determinar cor
        fb = self._balanceamento(no)
        
        if self.destaque_no and no.valor == self.destaque_no:
            cor = 'gold'  # Amarelo para destaque
        elif abs(fb) > 1:
            cor = 'lightcoral'  # Vermelho para desbalanceado
        else:
            cor = 'lightgreen'  # Verde para balanceado
        
        # Desenhar linhas para os filhos primeiro (para ficarem atrás)
        if no.esquerda:
            x_esq = x - dx
            y_esq = y - 1
            ax.plot([x, x_esq], [y, y_esq], 'k-', linewidth=2, zorder=1)
            self._desenhar_no(ax, no.esquerda, x_esq, y_esq, dx/2)
        
        if no.direita:
            x_dir = x + dx
            y_dir = y - 1
            ax.plot([x, x_dir], [y, y_dir], 'k-', linewidth=2, zorder=1)
            self._desenhar_no(ax, no.direita, x_dir, y_dir, dx/2)
        
        # Desenhar o nó (círculo)
        circle = plt.Circle((x, y), 0.15, color=cor, ec='black', linewidth=2, zorder=2)
        ax.add_patch(circle)
        
        # Texto do valor
        ax.text(x, y, str(no.valor), ha='center', va='center',
               fontsize=12, fontweight='bold', zorder=3)
        
        # Texto FB e altura (abaixo do nó)
        ax.text(x, y-0.25, f'FB:{fb} h:{no.altura}',
               ha='center', va='top', fontsize=8, color='darkblue', zorder=3)

    def adicionar_no(self, valor):
        """Adiciona um nó na árvore"""
        self.mensagem = f"Adicionando: {valor}"
        
        if self.vazia():
            self.raiz = No(valor)
            self.destaque_no = valor
            self.visualizar(f"Primeiro Nó: {valor}")
            input("Pressione Enter para continuar...")
            return
        
        print(f"\n{'='*50}")
        print(f"Adicionando: {valor}")
        print('='*50)
        self.raiz = self._adicionar_no_folha(self.raiz, valor)
        self.destaque_no = None
        self.mensagem = f"Nó {valor} adicionado!"
        self.visualizar(f"Árvore após adicionar {valor}")

    def _adicionar_no_folha(self, no_atual, valor):
        """Adiciona recursivamente e balanceia"""
        if not no_atual:
            novo_no = No(valor)
            self.destaque_no = valor
            self.mensagem = f"Novo nó criado: {valor}"
            self.visualizar(f"Novo Nó: {valor}")
            input("Enter...")
            return novo_no
        
        # Navegar
        if valor < no_atual.valor:
            no_atual.esquerda = self._adicionar_no_folha(no_atual.esquerda, valor)
        else:
            no_atual.direita = self._adicionar_no_folha(no_atual.direita, valor)
        
        # Atualizar altura
        no_atual.altura = 1 + max(self._altura(no_atual.esquerda),
                                   self._altura(no_atual.direita))
        
        # Balanceamento
        fb = self._balanceamento(no_atual)
        
        self.destaque_no = no_atual.valor
        self.mensagem = f"Nó {no_atual.valor} - FB: {fb}, Altura: {no_atual.altura}"
        self.visualizar("Verificando Balanceamento")
        
        # Rotações
        if fb < -1:
            if valor < no_atual.esquerda.valor:
                # Caso EE
                self.mensagem = f"Desbalanceamento EE! FB={fb}"
                self.visualizar("Rotação Direita Necessária")
                input("Enter para rotacionar...")
                return self._rotacao_direita(no_atual)
            else:
                # Caso ED
                self.mensagem = f"Desbalanceamento ED! FB={fb}"
                self.visualizar("Rotação Dupla ED")
                input("Enter para rotacionar...")
                no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
                return self._rotacao_direita(no_atual)
        
        if fb > 1:
            if valor > no_atual.direita.valor:
                # Caso DD
                self.mensagem = f"Desbalanceamento DD! FB={fb}"
                self.visualizar("Rotação Esquerda Necessária")
                input("Enter para rotacionar...")
                return self._rotacao_esquerda(no_atual)
            else:
                # Caso DE
                self.mensagem = f"Desbalanceamento DE! FB={fb}"
                self.visualizar("Rotação Dupla DE")
                input("Enter para rotacionar...")
                no_atual.direita = self._rotacao_direita(no_atual.direita)
                return self._rotacao_esquerda(no_atual)
        
        return no_atual

    def _altura(self, no):
        return 0 if not no else no.altura

    def _balanceamento(self, no):
        if not no:
            return 0
        return self._altura(no.direita) - self._altura(no.esquerda)

    def _rotacao_esquerda(self, pai):
        """Rotação à esquerda"""
        self.mensagem = "ANTES da Rotação Esquerda"
        self.destaque_no = pai.valor
        self.visualizar("Antes: Rotação Esquerda")
        
        filhoD = pai.direita
        neto = filhoD.esquerda
        
        # Rotacionar
        filhoD.esquerda = pai
        pai.direita = neto
        
        # Atualizar alturas
        pai.altura = 1 + max(self._altura(pai.esquerda), self._altura(pai.direita))
        filhoD.altura = 1 + max(self._altura(filhoD.esquerda), self._altura(filhoD.direita))
        
        self.mensagem = "APÓS Rotação Esquerda"
        self.destaque_no = filhoD.valor
        self.visualizar("Depois: Rotação Esquerda")
        input("Enter...")
        
        return filhoD

    def _rotacao_direita(self, pai):
        """Rotação à direita"""
        self.mensagem = "ANTES da Rotação Direita"
        self.destaque_no = pai.valor
        self.visualizar("Antes: Rotação Direita")
        
        filhoE = pai.esquerda
        neto = filhoE.direita
        
        # Rotacionar
        filhoE.direita = pai
        pai.esquerda = neto
        
        # Atualizar alturas
        pai.altura = 1 + max(self._altura(pai.esquerda), self._altura(pai.direita))
        filhoE.altura = 1 + max(self._altura(filhoE.esquerda), self._altura(filhoE.direita))
        
        self.mensagem = "APÓS Rotação Direita"
        self.destaque_no = filhoE.valor
        self.visualizar("Depois: Rotação Direita")
        input("Enter...")
        
        return filhoE

    def remover_no(self, valor):
        """Remove um nó da árvore"""
        if self.vazia():
            print("Árvore vazia!")
            return
        
        print(f"\n{'='*50}")
        print(f"Removendo: {valor}")
        print('='*50)
        self.mensagem = f"Removendo: {valor}"
        self.destaque_no = valor
        self.visualizar(f"Removendo {valor}")
        input("Enter para iniciar...")
        
        self.raiz = self._remover_no(self.raiz, valor)
        self.destaque_no = None
        self.mensagem = f"Nó {valor} removido!"
        self.visualizar(f"Após remover {valor}")

    def _remover_no(self, no_atual, valor):
        """Remove recursivamente e balanceia"""
        if not no_atual:
            print("Valor não encontrado")
            return no_atual
        
        # Navegar
        if valor < no_atual.valor:
            no_atual.esquerda = self._remover_no(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            no_atual.direita = self._remover_no(no_atual.direita, valor)
        else:
            # Nó encontrado
            self.destaque_no = no_atual.valor
            self.mensagem = f"Nó encontrado: {valor}"
            self.visualizar("Nó Encontrado")
            input("Enter...")
            
            # Casos de remoção
            if no_atual.esquerda is None:
                return no_atual.direita
            elif no_atual.direita is None:
                return no_atual.esquerda
            
            # Dois filhos - usar sucessor
            temp = self._no_minimo(no_atual.direita)
            self.mensagem = f"Sucessor: {temp.valor}"
            self.visualizar("Sucessor Encontrado")
            input("Enter...")
            
            no_atual.valor = temp.valor
            no_atual.direita = self._remover_no(no_atual.direita, temp.valor)
        
        if no_atual is None:
            return no_atual
        
        # Atualizar altura
        no_atual.altura = 1 + max(self._altura(no_atual.esquerda),
                                   self._altura(no_atual.direita))
        
        # Rebalancear
        fb = self._balanceamento(no_atual)
        
        # Rotações
        if fb < -1 and self._balanceamento(no_atual.esquerda) <= 0:
            return self._rotacao_direita(no_atual)
        
        if fb < -1 and self._balanceamento(no_atual.esquerda) > 0:
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)
        
        if fb > 1 and self._balanceamento(no_atual.direita) >= 0:
            return self._rotacao_esquerda(no_atual)
        
        if fb > 1 and self._balanceamento(no_atual.direita) < 0:
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)
        
        return no_atual

    def _no_minimo(self, no):
        """Encontra o menor nó"""
        atual = no
        while atual.esquerda:
            atual = atual.esquerda
        return atual


def menu_interativo():
    """Menu principal"""
    arvore = ArvoreAVLVisual()
    
    while True:
        print("\n" + "="*50)
        print("ÁRVORE AVL - VISUALIZAÇÃO GRÁFICA")
        print("="*50)
        print("1. Adicionar valor")
        print("2. Remover valor")
        print("3. Visualizar árvore")
        print("4. Demo automática")
        print("5. Reiniciar")
        print("0. Sair")
        print("="*50)
        
        try:
            opcao = input("\nOpção: ").strip()
            
            if opcao == "1":
                valor = int(input("Valor: "))
                arvore.adicionar_no(valor)
            
            elif opcao == "2":
                valor = int(input("Valor: "))
                arvore.remover_no(valor)
            
            elif opcao == "3":
                arvore.mensagem = "Visualização atual"
                arvore.destaque_no = None
                arvore.visualizar("Árvore AVL Atual")
                input("\nEnter para continuar...")
            
            elif opcao == "4":
                print("\nDemo: Inserindo valores [50, 30, 70, 20, 40, 60, 80]")
                input("Enter para começar...")
                for v in [50, 30, 70, 20, 40, 60, 80]:
                    arvore.adicionar_no(v)
            
            elif opcao == "5":
                plt.close(arvore.fig)  # Fechar figura antiga
                arvore = ArvoreAVLVisual()
                print("Árvore reiniciada!")
            
            elif opcao == "0":
                plt.close('all')
                print("Encerrando...")
                break
            
            else:
                print("Opção inválida!")
        
        except ValueError:
            print("Erro: Digite um número válido!")
        except KeyboardInterrupt:
            plt.close('all')
            print("\nEncerrando...")
            break
        except Exception as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    print("\n" + "="*50)
    print("🌳 ÁRVORE AVL - VISUALIZAÇÃO GRÁFICA")
    print("="*50)
    print("\nCores:")
    print("  🟢 Verde = Balanceado")
    print("  🔴 Vermelho = Desbalanceado")
    print("  🟡 Amarelo = Destaque")
    print("="*50)
    input("\nPressione Enter para começar...")
    
    menu_interativo()
