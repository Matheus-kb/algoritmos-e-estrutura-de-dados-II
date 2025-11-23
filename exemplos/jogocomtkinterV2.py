
"""
Jogo de Damas - Versão Completa com Tkinter
Criado do zero com interface gráfica moderna
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext
import math

from abc import ABC


class Peca(ABC):
    id_peca = 0

    @classmethod
    def gerar_id(cls):
        cls.id_peca += 1
        return cls.id_peca


class Jogada:
    def __init__(self, origem: tuple, destino: tuple, tipo: str):
        self.id_jogada = Peca.gerar_id()
        self.origem = origem
        self.destino = destino
        self.tipo = tipo  # 'movimento' ou 'captura'
        self.filho_esquerdo = None
        self.filho_direito = None


class ArvoreDeJogadas:
    def __init__(self):
        self.raiz = None

    def inserir_jogada(self, nova_jogada: Jogada):
        if self.raiz is None:
            self.raiz = nova_jogada
        else:
            self._inserir(self.raiz, nova_jogada)

    def _inserir(self, atual: Jogada, nova_jogada: Jogada):
        if atual.destino == nova_jogada.origem:
            if nova_jogada.tipo == 'movimento':
                if atual.filho_esquerdo is None:
                    atual.filho_esquerdo = nova_jogada
                else:
                    self._inserir(atual.filho_esquerdo, nova_jogada)
            elif nova_jogada.tipo == 'captura':
                if atual.filho_direito is None:
                    atual.filho_direito = nova_jogada
                else:
                    self._inserir(atual.filho_direito, nova_jogada)
        else:
            if atual.filho_esquerdo:
                self._inserir(atual.filho_esquerdo, nova_jogada)
            if atual.filho_direito:
                self._inserir(atual.filho_direito, nova_jogada)

    def exibir_in_ordem(self):
        def _in_ordem(no):
            if no:
                _in_ordem(no.filho_esquerdo)
                print(f"{no.tipo.upper()}: {no.origem} → {no.destino}")
                _in_ordem(no.filho_direito)

        _in_ordem(self.raiz)

    def buscar_por_destino(self, destino: tuple) -> Jogada:
        def _buscar(no):
            if no is None:
                return None
            if no.destino == destino:
                return no
            return _buscar(no.filho_esquerdo) or _buscar(no.filho_direito)

        return _buscar(self.raiz)

    def caminho_agressivo(self):
        caminho = []
        atual = self.raiz
        while atual:
            caminho.append(f"{atual.tipo.upper()}: {atual.origem} → {atual.destino}")
            atual = atual.filho_direito
        for passo in caminho:
            print(passo)


class JogoDamas:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🎮 Jogo de Damas")
        self.root.geometry("1000x700")
        self.root.configure(bg='#1a1a1a')

        # Estado do jogo
        self.tabuleiro = [[None for _ in range(8)] for _ in range(8)]
        self.jogador = 'P'  # P = Pretas, B = Brancas
        self.jogada_origem = None
        self.jogada_destino = None
        self.tipo_jogada = "movimento"

        # Árvore de jogadas
        self.arvore = ArvoreDeJogadas()
        self.todas_jogadas = []  # Lista para manter todas as jogadas

        self.inicializar_tabuleiro()
        self.criar_interface()
        self.atualizar_display()

    def inicializar_tabuleiro(self):
        """Inicializa o tabuleiro com as peças nas posições corretas"""
        # Peças pretas (P) nas primeiras 3 linhas
        for linha in range(3):
            for coluna in range(8):
                if (linha + coluna) % 2 == 1:  # Apenas casas pretas
                    self.tabuleiro[linha][coluna] = 'P'

        # Peças brancas (B) nas últimas 3 linhas
        for linha in range(5, 8):
            for coluna in range(8):
                if (linha + coluna) % 2 == 1:  # Apenas casas pretas
                    self.tabuleiro[linha][coluna] = 'B'

    def criar_interface(self):
        """Cria a interface gráfica"""
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#1a1a1a')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Frame do tabuleiro
        board_frame = tk.Frame(main_frame, bg='#2d2d2d', relief=tk.RAISED, bd=3)
        board_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 20))

        # Título
        title_label = tk.Label(board_frame, text="🎯 TABULEIRO DE DAMAS",
                               font=('Arial', 18, 'bold'),
                               bg='#2d2d2d', fg='white')
        title_label.pack(pady=15)

        # Canvas do tabuleiro
        self.board_canvas = tk.Canvas(board_frame, width=400, height=400,
                                      bg='#f8f9fa', relief=tk.SUNKEN, bd=3)
        self.board_canvas.pack(pady=15)
        self.board_canvas.bind("<Button-1>", self.on_board_click)

        # Controles
        controls_frame = tk.Frame(board_frame, bg='#2d2d2d')
        controls_frame.pack(pady=15)

        # Botões de tipo de jogada
        self.btn_movimento = tk.Button(controls_frame, text="📝 MOVIMENTO",
                                       command=lambda: self.set_tipo_jogada("movimento"),
                                       bg='#4CAF50', fg='blue', font=('Arial', 12, 'bold'),
                                       relief=tk.RAISED, bd=2, padx=15, pady=8)
        self.btn_movimento.pack(side=tk.LEFT, padx=8)

        self.btn_captura = tk.Button(controls_frame, text="⚔️ CAPTURA",
                                     command=lambda: self.set_tipo_jogada("captura"),
                                     bg='#f44336', fg='blue', font=('Arial', 12, 'bold'),
                                     relief=tk.RAISED, bd=2, padx=15, pady=8)
        self.btn_captura.pack(side=tk.LEFT, padx=8)

        # Status
        self.status_label = tk.Label(board_frame, text="",
                                     font=('Arial', 14, 'bold'),
                                     bg='#2d2d2d', fg='#ffeb3b')
        self.status_label.pack(pady=10)

        # Frame da árvore
        tree_frame = tk.Frame(main_frame, bg='#2d2d2d', relief=tk.RAISED, bd=3)
        tree_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Título da árvore
        tree_title = tk.Label(tree_frame, text="🌳 ÁRVORE DE JOGADAS",
                              font=('Arial', 18, 'bold'),
                              bg='#2d2d2d', fg='white')
        tree_title.pack(pady=15)

        # Canvas da árvore
        self.tree_canvas = tk.Canvas(tree_frame, width=400, height=300,
                                     bg='#f8f9fa', relief=tk.SUNKEN, bd=3)
        self.tree_canvas.pack(pady=15)

        # Botões da árvore
        tree_buttons_frame = tk.Frame(tree_frame, bg='#2d2d2d')
        tree_buttons_frame.pack(pady=15)

        self.btn_arvore_completa = tk.Button(tree_buttons_frame, text="📊 TODAS JOGADAS",
                                             command=self.mostrar_arvore_completa,
                                             bg='#2196F3', fg='blue', font=('Arial', 11, 'bold'),
                                             relief=tk.RAISED, bd=2, padx=12, pady=6)
        self.btn_arvore_completa.pack(side=tk.LEFT, padx=8)

        # Área de texto
        self.info_text = scrolledtext.ScrolledText(tree_frame, height=8, width=45,
                                                   bg='#1a1a1a', fg='white',
                                                   font=('Consolas', 10))
        self.info_text.pack(pady=15, padx=15, fill=tk.BOTH, expand=True)

        # Configurar tipo inicial
        self.set_tipo_jogada("movimento")

    def desenhar_tabuleiro(self):
        """Desenha o tabuleiro no canvas"""
        self.board_canvas.delete("all")

        cell_size = 50
        start_x = 10
        start_y = 10

        # Desenhar casas
        for linha in range(8):
            for coluna in range(8):
                x1 = start_x + coluna * cell_size
                y1 = start_y + linha * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size

                # Cor da casa
                if (linha + coluna) % 2 == 0:
                    cor = '#f8f9fa'  # Branco
                else:
                    cor = '#2c3e50'  # Preto

                self.board_canvas.create_rectangle(x1, y1, x2, y2,
                                                   fill=cor, outline='#34495e', width=2)

                # Desenhar peças
                peca = self.tabuleiro[linha][coluna]
                if peca:
                    centro_x = x1 + cell_size // 2
                    centro_y = y1 + cell_size // 2
                    raio = cell_size // 3

                    if peca == 'P':
                        cor_peca = '#e74c3c'  # Vermelho
                        cor_borda = '#c0392b'
                    else:
                        cor_peca = '#f39c12'  # Laranja
                        cor_borda = '#d68910'

                    self.board_canvas.create_oval(centro_x - raio, centro_y - raio,
                                                  centro_x + raio, centro_y + raio,
                                                  fill=cor_peca, outline=cor_borda, width=3)

                # Coordenadas
                coord_text = f"{linha},{coluna}"
                self.board_canvas.create_text(x1 + 8, y1 + 8, text=coord_text,
                                              font=('Arial', 8), fill='#7f8c8d')

        # Destacar seleção
        if self.jogada_origem:
            linha, coluna = self.jogada_origem
            x1 = start_x + coluna * cell_size
            y1 = start_y + linha * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            self.board_canvas.create_rectangle(x1, y1, x2, y2,
                                               outline='#ffeb3b', width=5)

    def desenhar_arvore(self):
        """Desenha a árvore de jogadas"""
        self.tree_canvas.delete("all")

        if not self.arvore.raiz:
            self.tree_canvas.create_text(200, 150, text="🌳 Nenhuma jogada ainda",
                                         font=('Arial', 16), fill='#7f8c8d')
            return

        # Desenhar árvore recursivamente
        node_width = 120
        node_height = 40
        level_height = 80
        start_x = 200
        start_y = 30

        self._desenhar_no_arvore(self.arvore.raiz, start_x, start_y, node_width, node_height, level_height, 0)

    def _desenhar_no_arvore(self, no, x, y, node_width, node_height, level_height, nivel):
        """Desenha um nó da árvore recursivamente"""
        if not no:
            return

        # Cor do nó baseada no tipo
        if no.tipo == 'movimento':
            cor_fundo = '#4CAF50'
            emoji = '📝'
        else:
            cor_fundo = '#f44336'
            emoji = '⚔️'

        # Desenhar nó
        x1 = x - node_width // 2
        y1 = y - node_height // 2
        x2 = x + node_width // 2
        y2 = y + node_height // 2

        # Sombra
        self.tree_canvas.create_rectangle(x1 + 2, y1 + 2, x2 + 2, y2 + 2,
                                          fill='#000000', outline='')

        # Nó principal
        self.tree_canvas.create_rectangle(x1, y1, x2, y2,
                                          fill=cor_fundo, outline='white', width=2)

        # Texto
        texto = f"{emoji} {no.origem}→{no.destino}"
        self.tree_canvas.create_text(x, y - 8, text=texto,
                                     font=('Arial', 9, 'bold'), fill='white')

        # Tipo
        tipo_texto = no.tipo.upper()
        self.tree_canvas.create_text(x, y + 8, text=tipo_texto,
                                     font=('Arial', 8), fill='white')

        # Desenhar filhos
        offset_x = node_width * (2 ** (3 - nivel)) // 3

        if no.filho_esquerdo:
            child_x = x - offset_x
            child_y = y + level_height

            # Linha para filho esquerdo
            self.tree_canvas.create_line(x, y + node_height // 2,
                                         child_x, child_y - node_height // 2,
                                         fill='white', width=2)

            self._desenhar_no_arvore(no.filho_esquerdo, child_x, child_y,
                                     node_width, node_height, level_height, nivel + 1)

        if no.filho_direito:
            child_x = x + offset_x
            child_y = y + level_height

            # Linha para filho direito
            self.tree_canvas.create_line(x, y + node_height // 2,
                                         child_x, child_y - node_height // 2,
                                         fill='white', width=2)

            self._desenhar_no_arvore(no.filho_direito, child_x, child_y,
                                     node_width, node_height, level_height, nivel + 1)

    def on_board_click(self, event):
        """Manipula cliques no tabuleiro"""
        cell_size = 50
        start_x = 10
        start_y = 10

        coluna = (event.x - start_x) // cell_size
        linha = (event.y - start_y) // cell_size

        if 0 <= linha < 8 and 0 <= coluna < 8:
            if self.jogada_origem is None:
                # Selecionar origem
                peca = self.tabuleiro[linha][coluna]
                if peca and peca == self.jogador:
                    self.jogada_origem = (linha, coluna)
                    self.atualizar_display()
                    self.info_text.insert(tk.END, f"✅ Origem selecionada: ({linha}, {coluna})\n")
                else:
                    self.info_text.insert(tk.END, f"❌ Casa inválida ou não é seu jogador\n")
            else:
                # Selecionar destino
                self.jogada_destino = (linha, coluna)
                self.executar_jogada()

    def executar_jogada(self):
        """Executa a jogada selecionada"""
        if self.jogada_origem and self.jogada_destino:
            origem_linha, origem_coluna = self.jogada_origem
            destino_linha, destino_coluna = self.jogada_destino

            # Validar jogada
            if self.validar_jogada():
                # Executar movimento
                peca = self.tabuleiro[origem_linha][origem_coluna]
                self.tabuleiro[origem_linha][origem_coluna] = None
                self.tabuleiro[destino_linha][destino_coluna] = peca

                # Captura
                if self.tipo_jogada == 'captura':
                    meio_linha = (origem_linha + destino_linha) // 2
                    meio_coluna = (origem_coluna + destino_coluna) // 2
                    self.tabuleiro[meio_linha][meio_coluna] = None

                # Criar objeto Jogada e inserir na árvore
                jogada = Jogada(self.jogada_origem, self.jogada_destino, self.tipo_jogada)
                self.arvore.inserir_jogada(jogada)
                self.todas_jogadas.append(jogada)  # Adicionar à lista de todas as jogadas

                # Log
                self.info_text.insert(tk.END,
                                      f"✅ Jogada executada: {self.tipo_jogada.upper()} de {self.jogada_origem} para {self.jogada_destino}\n")

                # Alternar jogador
                self.jogador = 'B' if self.jogador == 'P' else 'P'

                # Limpar seleção
                self.limpar_selecao()
                self.atualizar_display()

                # Verificar fim de jogo
                self.verificar_fim_jogo()
            else:
                self.info_text.insert(tk.END, f"❌ Jogada inválida!\n")
                self.limpar_selecao()

    def validar_jogada(self):
        """Valida se a jogada é válida"""
        origem_linha, origem_coluna = self.jogada_origem
        destino_linha, destino_coluna = self.jogada_destino

        # Verificar se está dentro do tabuleiro
        if not (0 <= destino_linha < 8 and 0 <= destino_coluna < 8):
            return False

        # Verificar se o destino é casa preta
        if (destino_linha + destino_coluna) % 2 == 0:
            return False

        # Verificar se o destino está vazio
        if self.tabuleiro[destino_linha][destino_coluna] is not None:
            return False

        # Verificar movimento diagonal
        delta_linha = abs(destino_linha - origem_linha)
        delta_coluna = abs(destino_coluna - origem_coluna)

        if delta_linha != delta_coluna:
            return False

        # Verificar distância
        if self.tipo_jogada == 'movimento':
            if delta_linha != 1:
                return False
        elif self.tipo_jogada == 'captura':
            if delta_linha != 2:
                return False

            # Verificar se há adversário para capturar
            meio_linha = (origem_linha + destino_linha) // 2
            meio_coluna = (origem_coluna + destino_coluna) // 2
            adversario = self.tabuleiro[meio_linha][meio_coluna]

            if adversario is None or adversario == self.jogador:
                return False

        return True

    def set_tipo_jogada(self, tipo):
        """Define o tipo da jogada"""
        self.tipo_jogada = tipo
        if tipo == "movimento":
            self.btn_movimento.configure(bg='#45a049', relief=tk.SUNKEN)
            self.btn_captura.configure(bg='#f44336', relief=tk.RAISED)
        else:
            self.btn_movimento.configure(bg='#4CAF50', relief=tk.RAISED)
            self.btn_captura.configure(bg='#da190b', relief=tk.SUNKEN)

    def limpar_selecao(self):
        """Limpa a seleção atual"""
        self.jogada_origem = None
        self.jogada_destino = None
        self.atualizar_display()

    def mostrar_arvore_completa(self):
        """Mostra todas as jogadas realizadas"""
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(tk.END, "🌳 TODAS AS JOGADAS REALIZADAS:\n")
        self.info_text.insert(tk.END, "=" * 50 + "\n")

        if self.todas_jogadas:
            for i, jogada in enumerate(self.todas_jogadas, 1):
                self.info_text.insert(tk.END, f"{i}. {jogada.tipo.upper()}: {jogada.origem} → {jogada.destino}\n")

            self.info_text.insert(tk.END, f"\n📊 Total de jogadas: {len(self.todas_jogadas)}\n")
        else:
            self.info_text.insert(tk.END, "Nenhuma jogada realizada ainda.\n")

    def verificar_fim_jogo(self):
        """Verifica se o jogo terminou"""
        pretas = sum(1 for linha in self.tabuleiro for casa in linha if casa == 'P')
        brancas = sum(1 for linha in self.tabuleiro for casa in linha if casa == 'B')

        if pretas == 0:
            messagebox.showinfo("🏆 Fim de Jogo!", "Brancas venceram!\nTodas as peças pretas foram capturadas!")
        elif brancas == 0:
            messagebox.showinfo("🏆 Fim de Jogo!", "Pretas venceram!\nTodas as peças brancas foram capturadas!")

    def atualizar_display(self):
        """Atualiza toda a interface"""
        self.desenhar_tabuleiro()
        self.desenhar_arvore()

        # Atualizar status
        pretas = sum(1 for linha in self.tabuleiro for casa in linha if casa == 'P')
        brancas = sum(1 for linha in self.tabuleiro for casa in linha if casa == 'B')
        status_text = f"🎯 Jogador: {self.jogador} | Pretas: {pretas} | Brancas: {brancas}"
        self.status_label.configure(text=status_text)

    def executar(self):
        """Inicia o jogo"""
        self.root.mainloop()


if __name__ == "__main__":
    jogo = JogoDamas()
    jogo.executar()
