# -*- coding: utf-8 find path

graph = { 
    'a': ['c'], 
    'b': ['d'], 
    'c': ['e'], 
    'd': ['a', 'd'], 
    'e': ['b', 'c'] 
} 
  
# function to find path 
  
  
def find_path(graph, start, end, path=[]): 
    path = path + [start] 
    if start == end: 
        return path 
    for node in graph[start]: 
        if node not in path: 
            newpath = find_path(graph, node, end, path) 
            if newpath: 
                return newpath 
  
  
# Driver function call to print the path 
print(find_path(graph, 'd', 'c')) 


print('The path from vertex "a" to vertex "b":')
path = find_path(graph,'a', 'b')
print(path)

print('The path from vertex "a" to vertex "f":')
path = find_path(graph,'a', 'e')
print(path)

print('The path from vertex "a" to vertex "f":')
path = find_path(graph,"a", "f")
print(path)


print('The path from vertex "a" to vertex "d":')
path = find_path(graph,"a", "d")
print(path)

print('The path from vertex "c" to vertex "c":')
path = find_path(graph,"c", "c")
print(path)
