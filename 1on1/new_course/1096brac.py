import itertools


class Solution:
    def braceExpansionII(self, E: str) -> List[str]:
        stack = [[]]
        chars = ""
        pros = [""]
        tmp = []
        for i in range(len(E)):
            if E[i] == "{":
                if len(pros) > len(stack):  # 如果还有内层没破 累加
                    prev_pro = pros.pop()
                    product = ["".join(c) for c in itertools.product(
                        prev_pro, [chars])] if chars else prev_pro
                    pros.append(product)
                    tmp = []
                    chars = ""
                else:  # 如果是保持平衡的 直接向内 同时加stack和pros
                    stack.append(tmp)
                    pros.append(chars)
                    tmp = []
                    chars = ""
                    print("stack:", stack)
            elif E[i] != "}" and E[i] != ",":
                chars += E[i]
            elif E[i] == ",":
                if chars:
                    tmp.append(chars)
                chars = ""
            elif E[i] == "}":
                if chars:
                    tmp.append(chars)
                prev_pro = pros.pop()
                print("prev_pro:", prev_pro, "tmp:", tmp)
                product = ["".join(c) for c in itertools.product(
                    prev_pro, tmp)] if prev_pro else tmp
                print("product:", product)

                if i+1 < len(E):
                    if E[i+1] == "," or E[i+1] == "}":  # 内层破 向外合并
                        # print("here!")
                        tmp = stack.pop()+product  # len(stack) == len(pros)
                        chars = ""
                    else:
                        pros.append(product)  # 没破  pros变多
                        tmp = []
                        chars = ""
                else:
                    if stack:
                        tmp = stack.pop()+product
                    else:
                        tmp = product
                    chars = ""
        print("stack:", stack, "pros:", pros)
        tmp = ["".join(c) for c in itertools.product(
            pros[-1], tmp)] if pros[-1] else tmp
        res = list(set(tmp))
        res.sort()
        return res
