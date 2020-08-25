import re
str = "$50 each. $100, $999"
#res = re.sub(r"[$0-9]", str.lower().split)
print("find:", str.find("$"))
print("split:", str.split("$"))
