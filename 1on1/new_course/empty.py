import re
str = "$50 each. $100, $999"
#res = re.sub(r"[$0-9]", str.lower().split)
print("find:", str.find("$"))
print("split:", str.split("$"))

lst = [[1, 2], [3, 4], [5, 6]]
for u, v in lst[::-1]:
    print("u:", u, "v:", v)
