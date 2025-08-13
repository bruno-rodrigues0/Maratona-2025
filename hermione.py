def main():
    def encontrar_posicao(L, C, mapa):
        last_dir = ''
        # Encontra a posição inicial de Hermione ('o')
        for i in range(L):
            for j in range(C):
                if mapa[i][j] == 'o':
                    linha, coluna = i, j
                    break
        
        # Se movimenta
        while True:
            # sobe
            if linha > 0 and mapa[linha - 1][coluna] == 'H' and last_dir != 'baixo':
                linha -= 1
                last_dir = 'cima'
            #desce
            elif linha < L - 1 and mapa[linha + 1][coluna] == 'H' and last_dir != 'cima':
                linha += 1
                last_dir = 'baixo'
            # esquerda
            elif coluna > 0 and mapa[linha][coluna - 1] == 'H' and last_dir != 'direita':
                coluna -= 1
                last_dir = 'esquerda'
            # direita
            elif coluna < C - 1 and mapa[linha][coluna + 1] == 'H' and last_dir != 'esquerda':
                coluna += 1
                last_dir = 'direita'
            else:
                break  # Se não encontrar mais 'H', termina o loop
        
        return linha + 1, coluna + 1

    L, C = map(int, input().split()) # Linha e colunas
    mapa = [list(input()) for _ in range(L)]  # Mapa

    linha, coluna = encontrar_posicao(L, C, mapa)
    print(linha, coluna)

if __name__ == "__main__":
    main()
