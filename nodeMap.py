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
    edgeCount = 0
    lastNode = ""
    for x in nodeTrack.values():
        for y, z in x.items():
            nodeName = z
            n = pydot.Node(str(z), label=nodeName, color="green", fontcolor="white")
            graph.add_node(n)
            edgeCount += 1
            if edgeCount > 0:
                e = pydot.Edge(src=lastNode.get("label"), dst=n.get("label"))
                graph.add_edge(e)
            else:
                lastNode = n


while newLevel == "y":
    makeNode()
    newLevel = input("New LeveL? [y/n]")
    level += 1
graphNode()
graph.write_png("basic.png")
s.run(["start", "basic.png"], shell=True)
