import itertools


class Solution:
    def braceExpansionII(self, E: str) -> List[str]:
        if "{" not in E:
            return [E]
        stack = [[]]
        chars = ""
        pros = [""]
        tmp = []
        switch = False
        for i in range(len(E)):
            if E[i] == "{":
                if switch:  # 如果还有内层没破 累加
                    prev_pro = pros.pop()
                    product = ["".join(c) for c in itertools.product(
                        prev_pro, [chars])] if chars else prev_pro
                    print("new_Pro:", product, "switch false!")
                    pros.append(product)
                    tmp = []
                    chars = ""
                    switch = False
                else:
                    # if not tmp and chars:
                    #     switch = True
                    stack.append(tmp)
                    pros.append([chars])
                    tmp = []
                    chars = ""
                    #swtich = True
                    #print("stack:", stack)
            elif E[i] != "}" and E[i] != ",":
                chars += E[i]
                if i == len(E)-1 and switch:
                    prev_pro = pros.pop()
                    product = ["".join(c) for c in itertools.product(
                        prev_pro, [chars])] if chars else prev_pro
                    tmp = stack.pop()+product
            elif E[i] == ",":
                if switch:
                    print("counter the ,")
                    prev_pro = pros.pop()
                    product = ["".join(c) for c in itertools.product(
                        prev_pro, [chars])] if chars else prev_pro
                    tmp += product
                    # pros.append(product)
                    switch = False
                else:
                    if chars:
                        tmp.append(chars)
                chars = ""
            elif E[i] == "}":
                if chars:
                    tmp.append(chars)
                if pros:
                    prev_pro = pros.pop()
                print("prev_pro:", prev_pro, "tmp:", tmp)
                product = ["".join(c) for c in itertools.product(
                    prev_pro, tmp)] if prev_pro else tmp
                print("product:", product)

                if i+1 < len(E):
                    if E[i+1] == "," or E[i+1] == "}":  # 内层破 向外合并
                        tmp = stack.pop()+product  # len(stack) == len(pros)
                        print("broke here!", "tmp:", tmp)
                        chars = ""
                    else:
                        print("swtich True!")
                        # 破了一层但是后面还有连续 len(stack)还是==len(pros)  更新pros[-1]
                        pros.append(product)
                        tmp = []
                        chars = ""
                        switch = True
                else:
                    if stack:
                        tmp = stack.pop()+product
                    else:
                        tmp = product
                    #chars = ""
        print("stack:", stack, "pros:", pros, "tmp:", tmp, "chars:", chars)
        #tmp = ["".join(c) for c in itertools.product(tmp, chars)] if chars else tmp
        tmp = stack.pop()+tmp
        res = list(set(tmp))
        res.sort()
        return res
