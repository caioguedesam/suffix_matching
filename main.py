import tree

def ParseGenome(genome) -> str:
    split = genome.split('\n', 1)
    genome = split[1]
    genome = genome.replace('\n', '')
    return genome

# Retorna a maior substring que se repete no texto, junto com sua posição no texto
# e o número de ocorrências.
def GetLongestRepeatedSubstring(text):
    # Criando árvore de sufixos.
    t = tree.Tree(text)

    # Pegando resultados da busca na árvore.
    node = t.Search()
    result = node.GetAccumulatedSubstring(text) + [node.GetChildCount()]
    return result


file = open("sarscov2.fasta", "r")
genomeParsed = ParseGenome(file.read())
print(str(GetLongestRepeatedSubstring(genomeParsed)))
