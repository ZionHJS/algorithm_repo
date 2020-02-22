start = []
end = [1, 2, 3, 4, 5, 6]
print("combine:", start+end)

graph = {}
graph[1] = [2, 3]
if 1 in graph:
    print("graph:", graph)
if 2 not in graph:
    print("not in")
