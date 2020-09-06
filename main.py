import re
import tree

def parseGenome(genome) -> str:
    split = genome.split('\n', 1)
    genome = split[1]
    genome = re.sub('\n', '', genome)
    return genome

file = open("sarscov2.fasta", "r")
genomeParsed = parseGenome(file.read())
t = tree.Tree('abcxab')
t.PrintTree()
t.Search()