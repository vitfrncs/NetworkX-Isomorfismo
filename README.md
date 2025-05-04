
# Verificação de Isomorfismo de Grafos com NetworkX

Este repositório demonstra como utilizar a biblioteca [NetworkX](https://networkx.org/) para verificar se dois grafos são isomorfos. São apresentados conceitos, funções específicas da biblioteca e exemplos visuais comparando grafos diferentes e semelhantes.

## Conceitos Utilizados

### could_be_isomorphic(G1, G2)
Essa função realiza uma verificação **superficial** entre dois grafos. Ela **retorna `False`** se os grafos não forem isomorfos com certeza. Porém, se retornar `True`, **não garante** que os grafos sejam isomorfos. 

É útil para **descartar rapidamente pares de grafos** que claramente não são isomorfos com base em critérios como:

- Sequência de graus dos vértices
- Número de triângulos por nó
- Sequência de cliques máximos por nó

> 💡 **Clique máximo**: Conjunto de vértices que formam um subgrafo completamente conectado e que não pode ser expandido sem perder essa propriedade.

---

### is_isomorphic(G1, G2, node_match=None, edge_match=None)
Essa função faz uma verificação **completa e exata** de isomorfismo, utilizando o algoritmo **VF2**, que tenta encontrar uma bijeção entre os nós dos dois grafos, preservando:

- Conectividade entre os nós
- Graus dos nós
- (Opcionalmente) Atributos dos vértices e arestas

### Como o algoritmo VF2 funciona:

1. Começa sem nenhum nó pareado.
2. Escolhe um nó de `G1` e tenta emparelhá-lo com um nó de `G2`.
3. Verifica:
   - Vizinhança compatível
   - Graus semelhantes
   - (Se houver) Atributos iguais
4. Se a associação for válida, avança para o próximo nó.
5. Se falhar, faz *backtracking* e tenta outra combinação.
6. Se todos forem pareados com sucesso, os grafos são isomorfos.

---

## Dependências

- `networkx`
- `matplotlib`

Instale com:

```bash
pip install networkx matplotlib
```

---

## 🚀 Execução

Execute o script Python principal para visualizar e analisar exemplos:

```bash
python isomorfismo.py
```

---

## 🖼️ Visualização dos Grafos

Utilizamos `matplotlib` para desenhar os pares de grafos lado a lado, facilitando a comparação visual.


