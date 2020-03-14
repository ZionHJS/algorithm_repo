from collections import defaultdict
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
g = defaultdict(list)
print("g:", g)

log = "dig1 8 1 5 1"
fidx = log.find(" ")
print("fidx:", fidx)


def g(x):
    return (x[x.find(" "):], x[:x.find(" ")])


logs = ["let1 art can", "let2 own kit dig", "let3 art zero"]
for log in logs:
    print("g(log):", g(log))
