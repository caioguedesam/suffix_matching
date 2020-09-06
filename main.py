import re

def parseGenome(genome) -> str:
    split = genome.split('\n', 1)
    genome = split[1]
    genome = re.sub('\n', '', genome)
    return genome

file = open("sarscov2.fasta", "r")
string = parseGenome(file.read())
print(string)