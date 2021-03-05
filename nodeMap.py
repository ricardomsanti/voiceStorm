import pydot
import subprocess as s

graph = pydot.Dot('my_graph', graph_type='graph', bgcolor="black", fgcolor="white", fontcolor="white", dpi=500)
g2 = pydot.Subgraph('my_sub', graph_type='graph', bgcolor="black", fgcolor="white", fontcolor="white", dpi=500)
nodeTrack = {}
levelTrack = {}
level = 0
newLevel = "y"

def makeNode():
    line = input("Side node numbers: ")
    for x in range(int(line)):
        nodeName = input("Please name node #{}".format(x))
        levelTrack.update({x: nodeName})
    nodeTrack.update({level: levelTrack})

def graphNode():
    edgeList = []
    for x in nodeTrack.values():
        for y, z in x.items():
            n = pydot.Node(str(z), label=str(z), color="green", fontcolor="white")
            edgeList.append(n)
            g2.add_node(n)
        graph.add_subgraph(g2)
        """for x in edgeList[1:len(edgeList)-1]:
            x_index = edgeList.index(x)
            edge = pydot.Edge(x.name, edgeList[x_index +1])
            graph.add_edge(edge)
"""



while newLevel == "y":
    makeNode()
    newLevel = input("New LeveL? [y/n]")
    level += 1
graphNode()
graph.write_png("basic.png")
s.run(["start", "basic.png"],  shell=True)