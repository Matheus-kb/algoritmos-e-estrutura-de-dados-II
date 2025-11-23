class Jogada:
    def __init__(self, origem: tuple, destino: tuple, tipo: str):
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

    def profundidade_maxima(self) -> int:
        def _profundidade(no):
            if no is None:
                return 0
            return 1 + max(_profundidade(no.filho_esquerdo), _profundidade(no.filho_direito))
        return _profundidade(self.raiz)

    def caminho_agressivo(self):
        caminho = []
        atual = self.raiz
        while atual:
            caminho.append(f"{atual.tipo.upper()}: {atual.origem} → {atual.destino}")
            atual = atual.filho_direito
        for passo in caminho:
            print(passo)


class TabuleiroDamas:
    def __init__(self):
        self.tabuleiro = [[None for _ in range(8)] for _ in range(8)]
        self.turno = 'P'
        self.inicializar()

    def inicializar(self):
        for linha in range(3):
            for coluna in range(8):
                if (linha + coluna) % 2 == 1:
                    self.tabuleiro[linha][coluna] = 'P'
        for linha in range(5, 8):
            for coluna in range(8):
                if (linha + coluna) % 2 == 1:
                    self.tabuleiro[linha][coluna] = 'B'

    def exibir(self):
        print("   " + " ".join(str(i) for i in range(8)))
        print("  +" + "---+" * 8)
        for i, linha in enumerate(self.tabuleiro):
            linha_str = f"{i} |"
            for casa in linha:
                if casa == 'P':
                    linha_str += " P |"
                elif casa == 'B':
                    linha_str += " B |"
                else:
                    linha_str += "   |"
            print(linha_str)
            print("  +" + "---+" * 8)

    def aplicar_jogadas_da_arvore(self, arvore):
        def aplicar_jogada(jogada):
            origem_linha, origem_coluna = jogada.origem
            destino_linha, destino_coluna = jogada.destino
            peca = self.tabuleiro[origem_linha][origem_coluna]

            if peca is None:
                print(f" Jogada inválida: não há peça em {jogada.origem}")
                return

            if peca != self.turno:
                print(f" Jogada inválida: é o turno de {self.turno}, mas tentou mover {peca}")
                return

            # Captura simples
            if jogada.tipo == 'captura':
                meio_linha = (origem_linha + destino_linha) // 2
                meio_coluna = (origem_coluna + destino_coluna) // 2
                adversaria = self.tabuleiro[meio_linha][meio_coluna]

                if adversaria is None or adversaria == peca:
                    print(f" Captura inválida: sem adversário em {(meio_linha, meio_coluna)}")
                    return

                self.tabuleiro[meio_linha][meio_coluna] = None

            self.tabuleiro[origem_linha][origem_coluna] = None
            self.tabuleiro[destino_linha][destino_coluna] = peca
            print(f"Jogada aplicada: {jogada.tipo.upper()} de {jogada.origem} para {jogada.destino}")

            # Alterna o turno
            self.turno = 'B' if self.turno == 'P' else 'P'

        def percorrer_e_aplicar(no):
            if no is None:
                return
            aplicar_jogada(no)
            self.exibir()
            percorrer_e_aplicar(no.filho_esquerdo)
            percorrer_e_aplicar(no.filho_direito)

        print("\nAplicando jogadas da árvore:")
        percorrer_e_aplicar(arvore.raiz)

    def aplicar_jogada_individual(self, jogada):
        origem_linha, origem_coluna = jogada.origem
        destino_linha, destino_coluna = jogada.destino
        peca = self.tabuleiro[origem_linha][origem_coluna]

        if peca is None:
            print(f"Jogada inválida: não há peça em {jogada.origem}")
            return

        if peca != self.turno:
            print(f"Jogada inválida: é o turno de {self.turno}, mas tentou mover {peca}")
            return

        if jogada.tipo == 'captura':
            meio_linha = (origem_linha + destino_linha) // 2
            meio_coluna = (origem_coluna + destino_coluna) // 2
            adversaria = self.tabuleiro[meio_linha][meio_coluna]

            if adversaria is None or adversaria == peca:
                print(f"Captura inválida: sem adversário em {(meio_linha, meio_coluna)}")
                return

            self.tabuleiro[meio_linha][meio_coluna] = None

        self.tabuleiro[origem_linha][origem_coluna] = None
        self.tabuleiro[destino_linha][destino_coluna] = peca
        print(f"Jogada aplicada: {jogada.tipo.upper()} de {jogada.origem} para {jogada.destino}")
        self.turno = 'B' if self.turno == 'P' else 'P'

    def realizar_jogadas(self, arvore):
        while True:
            print(f"\n🎯 Turno atual: jogador {self.turno}")
            print("""Como Digitar Exemplo: ol,oc-dl,dc-mo   ou ol,oc-dl-dc-ca 
                ol - origemLinha      oc - origemColuna
                dl - destinoLinha     dc - destinoColuna
                mo - movimento   ou   ca - captura 
                """)
            digitacao = input("Entre a jogada no formato:  ")
            origem, destino, acao = digitacao.split("-")
            olinha, ocoluna = origem.split(",")
            dlinha, dcoluna = destino.split(",")
            if acao == "mo":
                acao = "movimento"
            else:
                acao = "captura"
            jogada = Jogada((int(olinha), int(ocoluna)), (int(dlinha), int(dcoluna)), acao)
            arvore.inserir_jogada(jogada)
            self.aplicar_jogada_individual(jogada)
            self.exibir()



arvore = ArvoreDeJogadas()
tabuleiro = TabuleiroDamas()
tabuleiro.exibir()
tabuleiro.realizar_jogadas(arvore)


"""
    0   1   2   3   4   5   6   7
  +---+---+---+---+---+---+---+---+
0 |   | P |   | P |   | P |   | P |
  +---+---+---+---+---+---+---+---+
1 | P |   | P |   | P |   | P |   |
  +---+---+---+---+---+---+---+---+
2 |   | P |   | P |   | P |   | P |
  +---+---+---+---+---+---+---+---+
3 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
4 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
5 | B |   | B |   | B |   | B |   |
  +---+---+---+---+---+---+---+---+
6 |   | B |   | B |   | B |   | B |
  +---+---+---+---+---+---+---+---+
7 | B |   | B |   | B |   | B |   |
  +---+---+---+---+---+---+---+---+
  """