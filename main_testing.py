import sys
import tree
import time
from guppy import hpy

h = hpy()
startTime = time.time()

def PrintTimeAndMemoryAtInstant(message = ''):
    if message != '':
        print('{0}:'.format(message))
    print('+++ Tempo total: {:10.3f} segundos'.format(time.time() - startTime))
    print('+++ Memória utilizada: {:10.3f} megabytes'.format(h.heap().size / 1000000))

def ParseGenome(genome) -> str:
    split = genome.split('\n', 1)
    genome = split[1]
    genome = genome.replace('\n', '')
    return genome

# Retorna a maior substring que se repete no texto, junto com sua posição no texto
# e o número de ocorrências.
def GetLongestRepeatedSubstring(text):
    PrintTimeAndMemoryAtInstant('Antes de ler e armazenar o arquivo')
    # Criando árvore de sufixos.
    t = tree.Tree(text)
    PrintTimeAndMemoryAtInstant('Após construção da árvore de sufixos do texto')

    # Pegando resultados da busca na árvore.
    node = t.Search()
    result = node.GetAccumulatedSubstring(text) + [node.GetChildCount()]
    PrintTimeAndMemoryAtInstant('Após encontrar a maior substring repetida')
    return result

def TestCase(filePath = 'sarscov2.fasta'):
    print('Caso de teste: {0}'.format(filePath))
    file = open(filePath, "r")
    genomeParsed = ParseGenome(file.read())
    print(str(GetLongestRepeatedSubstring(genomeParsed)))

TestCase(sys.argv[1])