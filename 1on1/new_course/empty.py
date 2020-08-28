import re
str = "$50 each. $100, $999"
lst = re.findall(r"\$\d+", str.lower())
print("res:", lst)


print("find:", str.find("$"))
print("split:", str.split("$"))

lst = [[1, 2], [3, 4], [5, 6]]
for u, v in lst[::-1]:
    print("u:", u, "v:", v)
