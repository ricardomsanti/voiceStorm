import pydot as pd
from RecAndRead import RecAndRead
import subprocess as s

rr = RecAndRead()
text = "text"
graph = pd.Dot("mygraph", graph_type="graph",fgcolor="#00e600", backgroundcolor="#000000")

num = 0
rr.micPick()
while text != "":
    num += 1
    rr.saySomething(line="Novo ponto?")
    new = rr.listenTo()
    if new == "pára":
        break
    else:
        node = pd.Node(str(new),label=str(new),fgcolor="#000000", backgroundcolor="#00e600")
        graph.add_node(node)
        """
        if num > 0:
            #números ímpares
            if num % 2 != 0:
                n1 = baseNode
            else:
                n2 = baseNode
                baseEdge = pd.Edge(n1.get("name"), n2.get("name"))
               graph.add_edge(baseEdge)
        """

graph.write_png("newGraph.jpg")
s.run(["cmd start newGraph.jpg"], shell=True)