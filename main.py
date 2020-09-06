import tree

def ParseGenome(genome) -> str:
    split = genome.split('\n', 1)
    genome = split[1]
    genome = genome.replace('\n', '')
    return genome

def GetLongestRepeatedSubstring(text):
    # Creating suffix tree
    t = tree.Tree(text)

    # Fetching results from search in suffix tree
    node = t.Search()
    return [node.GetAccumulatedSubstring(text), node.start, node.GetChildCount()]


file = open("sarscov2.fasta", "r")
genomeParsed = ParseGenome(file.read())

print(str(GetLongestRepeatedSubstring(genomeParsed)))
