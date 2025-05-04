import networkx as nx
import matplotlib.pyplot as plt

# Função auxiliar para visualizar dois grafos lado a lado
# Recebe dois grafos (G1 e G2) e um título para a visualização
def mostrar_grafos(G1, G2, titulo): 
    plt.figure(figsize=(8, 4))  # Define o tamanho da figura

    # Desenha o primeiro grafo no lado esquerdo
    plt.subplot(121)
    nx.draw(G1, with_labels=True, node_color='lightgreen')
    plt.title("Grafo 1")

    # Desenha o segundo grafo no lado direito
    plt.subplot(122)
    nx.draw(G2, with_labels=True, node_color='lightblue')
    plt.title("Grafo 2")

    # Adiciona o título geral
    plt.suptitle(titulo)
    plt.show()

# --- Exemplo 1: Grafos não isomorfos ---
# G1 é um triângulo com uma aresta extra (nó 4 ligado ao nó 1)
G1 = nx.Graph()
G1.add_edges_from([(1, 2), (2, 3), (3, 1), (1, 4)])  

# G2 é um quadrado, sem triângulos
G2 = nx.Graph()
G2.add_edges_from([(5, 6), (6, 7), (7, 8), (8, 5)])  

# Mostra visualmente que as estruturas são diferentes
mostrar_grafos(G1, G2, "Exemplo 1: Estruturas diferentes")

# Verifica possibilidade de isomorfismo (análise superficial)
print("could_be_isomorphic:", nx.could_be_isomorphic(G1, G2))
# Verifica isomorfismo exato (análise completa)
print("is_isomorphic:", nx.is_isomorphic(G1, G2))
print("-" * 40)

# --- Exemplo 2: Verdadeiro positivo (isomorfismo real) ---
# G3 é um triângulo simples
G3 = nx.Graph()
G3.add_edges_from([(1, 2), (2, 3), (3, 1)])  

# G4 é outro triângulo com rótulos diferentes (mas mesma estrutura)
G4 = nx.Graph()
G4.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'a')])  

# Estruturas são idênticas, apesar dos rótulos diferentes
mostrar_grafos(G3, G4, "Exemplo 2: Isomorfismo real")

# Ambos devem retornar True
print("could_be_isomorphic:", nx.could_be_isomorphic(G3, G4))
print("is_isomorphic:", nx.is_isomorphic(G3, G4))

# --- Exemplo 3: Falso positivo ---
# G5 e G6 possuem o mesmo número de nós e graus compatíveis,
# mas suas estruturas internas são diferentes

# G5: grafo com bifurcações
G5 = nx.Graph()
G5.add_edges_from([
    ('A', 'B'), ('B', 'C'), ('B', 'D'),
    ('C', 'E'), ('D', 'F'), ('E', 'G'),
    ('F', 'H')
])

# G6: grafo com bifurcação mais distante
G6 = nx.Graph()
G6.add_edges_from([
    (1, 2), (2, 3), (2, 4), (4, 5),
    (5, 6), (6, 7), (7, 8)
])

# Apesar de parecidos na aparência superficial, não são isomorfos
mostrar_grafos(G5, G6, "Falso Positivo: could_be True, mas não são isomorfos")

# could_be_isomorphic pode retornar True,
# mas is_isomorphic detecta corretamente que são diferentes
print("could_be_isomorphic:", nx.could_be_isomorphic(G5, G6))
print("is_isomorphic:", nx.is_isomorphic(G5, G6))