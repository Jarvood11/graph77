# Python 3.9.5 (default, May 11 2021, 07:48:02)
# [GCC 10.3.0] on linux  https://pycomp.vercel.app/
# Type "help", "copyright", "credits" or "license" for more information.
graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges

print(generate_edges(graph))
#print("Hello, World!")
def find_isolated_nodes(graph):
    """ returns a list of isolated nodes. """
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated += node
    return isolated

print(find_isolated_nodes(graph))
