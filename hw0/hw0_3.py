import snap

data = snap.LoadEdgeList(snap.PNGraph, "stackoverflow-Java.txt", 0, 1, '\t')

# The number of weakly connected components in the network.
Components = snap.TCnComV()
snap.GetWccs(data, Components)
print("Number of Weakly Connected Components:", Components.Len())

# The number of edges and the number of nodes in the largest weakly connected component
MxWcc = snap.GetMxWcc(data)
print("Number of MxWcc Edges:", MxWcc.GetEdges())
print("Number of MxWcc Nodes:", MxWcc.GetNodes())

# IDs of the top 3 most central nodes in the network by PagePank scores
PRankH = snap.TIntFlt64H()
snap.GetPageRank(data, PRankH)
PRankH.SortByDat(False)

i = 0
itr = PRankH.BegI()
print("The top 3 most central nodes in the network by PagePank scores:")
while i < 3:
    print("Node:", itr.GetKey())
    itr.Next()
    i += 1
print("")

# IDs of the top 3 hubs and top 3 authorities in the network by HITS scores.
NIdHubH = snap.TIntFlt64H()
NIdAuthH = snap.TIntFlt64H()
snap.GetHits(data, NIdHubH, NIdAuthH)
NIdHubH.SortByDat(False)

i = 0
itr = NIdHubH.BegI()
print("The top 3 hubs in the network by HITS score:")
while i < 3:
    print("Node:", itr.GetKey())
    itr.Next()
    i += 1

