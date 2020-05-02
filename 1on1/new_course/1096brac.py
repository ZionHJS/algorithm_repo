import itertools


class Solution:
    def braceExpansionII(self, E: str) -> List[str]:
        stack = []
        chars = ""
        pros = []
        cur = []
        switch = False
        for i in range(len(E)):
            if E[i] == "{":
                if switch:  # 完全正确
                    prev_pro = pros.pop()
                    product = ["".join(c) for c in itertools.product(
                        prev_pro, [chars])] if chars else prev_pro
                    pros.append(product)
                    #print("{-switch:", "stack:", stack, "pros:", pros)
                    cur = []
                    chars = ""
                    switch = False
                else:  # 完全正确
                    stack.append(cur)
                    pros.append([chars])
                    #print("stack:", stack, "pros:", pros)
                    cur = []
                    chars = ""
            elif E[i] != "}" and E[i] != ",":
                chars += E[i]
                if i == len(E)-1:
                    if switch:
                        prev_pro = pros.pop()
                        product = ["".join(c) for c in itertools.product(
                            prev_pro, [chars])] if chars else prev_pro
                        cur += product
                    else:
                        cur.append(chars)
                #print("change chars:", chars)
            elif E[i] == ",":
                if switch:
                    prev_pro = pros.pop()
                    product = ["".join(c) for c in itertools.product(
                        prev_pro, [chars])] if chars else prev_pro
                    cur = stack.pop() + product
                    #print(",-switch-off-cur:", cur)
                    switch = False
                else:
                    if chars:
                        cur.append(chars)
                chars = ""
            elif E[i] == "}":  # out
                if switch:
                    prev_pro = pros.pop()
                    product = ["".join(c) for c in itertools.product(
                        prev_pro, [chars])] if prev_pro else cur
                if chars:
                    cur.append(chars)
                #print("chars:", chars, "cur:", cur)
                prev_pro = pros.pop()
                product = ["".join(c) for c in itertools.product(
                    prev_pro, cur)] if prev_pro else cur
                print("product:", product)
                if switch:
                    cur = stack.pop()+product
                    prev_pro = pros.pop()
                    product = ["".join(c) for c in itertools.product(
                        prev_pro, cur)] if prev_pro else cur
                    print("break-swtich:", "product:", product)
                    cur = product
                    switch = False
                    chars = ""
                else:
                    cur = product
                    chars = ""

                if i < len(E)-1:
                    if E[i+1] != "," and E[i+1] != "}":  # if next-switch
                        print("switch!", "cur:", cur)
                        pros.append(cur)
                        switch = True
                        chars = ""
                        cur = []
                    else:  # if next-not-swtich
                        cur = stack.pop()+cur
                        chars = ""

        print("stack:", stack, "pros:", pros, "cur:", cur, "chars:", chars)
        #if chars: cur.append(chars)
        # while pros:
        #     prev_pro = pros.pop()
        #     product = ["".join(c) for c in itertools.product(prev_pro, cur)] if prev_pro else cur
        #     cur = stack.pop() + product
        res = list(set(cur))
        res.sort()
        #print("stack:", stack, "pros:", pros, "cur:", cur, "chars:", chars)
        return res
