from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        Calcula o menor caminho de (0, 0) até (n-1, m-1) em uma grade com obstáculos,
        permitindo eliminar até 'k' obstáculos.
        """

        # Função para verificar se a célula está dentro dos limites da grade
        def posicao_valida(linha, coluna):
            return 0 <= linha < linhas and 0 <= coluna < colunas

        # Tamanho da grade
        linhas, colunas = len(grid), len(grid[0])

        # Fila para BFS: armazena (linha, coluna, obstaculos_restantes, passos)
        fila = deque([(0, 0, k, 0)])

        # Conjunto para registrar estados visitados (linha, coluna, obstáculos restantes)
        visitados = set()

        # Inicia a busca em largura
        while fila:
            linha, coluna, obstaculos_restantes, passos = fila.popleft()

            # Se chegarmos ao destino, retornamos o número de passos
            if (linha, coluna) == (linhas - 1, colunas - 1):
                return passos

            # Ignora estados já visitados
            if (linha, coluna, obstaculos_restantes) in visitados:
                continue

            # Marca o estado atual como visitado
            visitados.add((linha, coluna, obstaculos_restantes))

            # Verifica as células vizinhas
            for prox_linha, prox_coluna in [
                (linha - 1, coluna), 
                (linha, coluna - 1), 
                (linha + 1, coluna), 
                (linha, coluna + 1)
            ]:
                if not posicao_valida(prox_linha, prox_coluna):
                    continue

                # Se a célula vizinha é livre
                if grid[prox_linha][prox_coluna] == 0:
                    fila.append((prox_linha, prox_coluna, obstaculos_restantes, passos + 1))
                
                # Se a célula vizinha contém um obstáculo
                elif obstaculos_restantes > 0:
                    fila.append((prox_linha, prox_coluna, obstaculos_restantes - 1, passos + 1))

        # Se não encontramos um caminho, retornamos -1
        return -1
