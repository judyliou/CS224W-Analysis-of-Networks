import snap

wiki = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1, '\t')

# number of nodes
print("Node number:", wiki.GetNodes())

# number of self-edge
print("Self Edges:", snap.CntSelfEdges(wiki))

# number of directed edges
print("Directed Edges:", wiki.GetEdges()-snap.CntSelfEdges(wiki))

# number of undirected edges (A->B and B->A counts a single undirected edge)
print("Undirected Edges:", snap.CntUniqUndirEdges(wiki))

# number of reciprocated edges
print("Reciprocated Edges:", snap.CntUniqBiDirEdges(wiki))

# nubmber of nodes of zero out-degree
print("# of zero out-degree:", snap.CntOutDegNodes(wiki, 0))

# number of nodes of zero in-degree
print("# of zero in-degree:", snap.CntInDegNodes(wiki, 0))

# number of nodes with out-degree > 10
count = 0
for i in range(11):
    count += snap.CntOutDegNodes(wiki, i)
temp = wiki.GetNodes() - count 
print("Nodes with out-degree > 10:", temp)

# number of nodes with in-degree < 10
count = 0
for i in range(10):
    count += snap.CntInDegNodes(wiki, i)
print("Nodes with in-degree < 10:", count)
