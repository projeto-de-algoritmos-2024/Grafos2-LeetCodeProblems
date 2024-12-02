from heapq import heappop, heappush
from typing import List

def distancia_manhattan(ponto1: List[int], ponto2: List[int]) -> int:
    """
    Calcula a distância de Manhattan entre dois pontos.
    """
    return abs(ponto1[0] - ponto2[0]) + abs(ponto1[1] - ponto2[1])

class Solution:
    def minCostConnectPoints(self, pontos: List[List[int]]) -> int:
        """
        Calcula o custo mínimo para conectar todos os pontos usando o algoritmo de Prim
        para encontrar a Árvore Geradora Mínima (MST).
        """
        n = len(pontos)  # Número total de pontos
        visitados = [False] * n  # Marca os pontos já incluídos na MST
        menor_custo = {0: 0}  # Armazena o menor custo para conectar cada ponto
        fila_prioridade = [(0, 0)]  # Min-Heap inicializado com o ponto 0 e custo 0

        custo_total = 0  # Peso total da MST

        # Algoritmo de Prim
        while fila_prioridade:
            custo, ponto_atual = heappop(fila_prioridade)  # Remove o ponto com menor custo da fila

            # Ignora se o ponto já foi visitado ou se o custo não é o menor
            if visitados[ponto_atual] or menor_custo.get(ponto_atual, float('inf')) < custo:
                continue

            # Marca o ponto atual como visitado
            visitados[ponto_atual] = True
            custo_total += custo  # Adiciona o custo ao peso total da MST

            # Atualiza os custos dos pontos adjacentes
            for vizinho in range(n):
                if not visitados[vizinho]:  # Só considera pontos ainda não visitados
                    distancia = distancia_manhattan(pontos[ponto_atual], pontos[vizinho])

                    # Atualiza a distância se encontrarmos uma conexão mais barata
                    if distancia < menor_custo.get(vizinho, float('inf')):
                        menor_custo[vizinho] = distancia
                        heappush(fila_prioridade, (distancia, vizinho))

        return custo_total
