import itertools


class Solution:
    def braceExpansionII(self, E: str) -> List[str]:
        stack = []
        chars = ""
        pros = []
        cur = []
        switch = False
        for i in range(len(E)):
            if E[i] == "{":  # in
                if switch:
                    prev_pro = pros.pop()
                    product = ["".join(c) for c in itertools.product(
                        prev_pro, [chars])] if chars else prev_pro
                    pros.append(product)
                    # stack.append(cur)
                    print("{-switch:", "stack:", stack, "pros:", pros)
                    cur = []
                    chars = ""
                    switch = False
                else:
                    stack.append(cur)
                    pros.append([chars])
                    print("stack:", stack, "pros:", pros)
                    cur = []
                    chars = ""
            elif E[i] != "}" and E[i] != ",":
                chars += E[i]
                # if i == len(E)-1:
                #     if switch:
                #         prev_pro = pros.pop()
                #         product = ["".join(c) for c in itertools.product(prev_pro, [chars])] if chars else prev_pro
                #         cur += product
                #     else:
                #         cur.append(chars)
                print("change chars:", chars)
            elif E[i] == ",":
                if switch:
                    prev_pro = pros.pop()
                    product = ["".join(c) for c in itertools.product(
                        prev_pro, [chars])] if chars else prev_pro
                    #cur += product
                    cur = stack.pop() + cur + product
                    print(",-switch-off-cur:", cur)
                    switch = False
                else:
                    if chars:
                        cur.append(chars)
                chars = ""
            elif E[i] == "}":  # out
                if chars:
                    cur.append(chars)
                print("chars:", chars, "cur:", cur)
                prev_pro = pros.pop()
                product = ["".join(c) for c in itertools.product(
                    prev_pro, cur)] if prev_pro else cur
                print("product:", product)

                if i < len(E)-1:
                    if E[i+1] != "," and E[i+1] != "}":
                        if switch:
                            cur = stack.pop()+product
                            prev_pro = pros.pop()
                            print("switch!", "cur:", cur,
                                  "prev_pro:", prev_pro)
                            product = ["".join(c) for c in itertools.product(
                                prev_pro, cur)] if prev_pro else cur
                            pros.append(product)
                        else:
                            pros.append(product)
                            print("switch!", "pros:", pros)
                        switch = True
                        chars = ""
                        cur = []
                        #cur = stack.pop()
                    else:
                        cur = stack.pop()+product
                        chars = ""
                        print("break-cur:", cur)
                # else:
                #     cur=stack.pop()+product
                #     print("the last", "cur:", cur, "stack:", stack, "pros:", pros)

        print("stack:", stack, "pros:", pros, "cur:", cur, "chars:", chars)
        if chars:
            cur.append(chars)
        while pros:
            prev_pro = pros.pop()
            product = ["".join(c) for c in itertools.product(
                prev_pro, cur)] if prev_pro else cur
            cur = stack.pop() + product
        res = list(set(cur))
        # res.sort()
        #print("stack:", stack, "pros:", pros, "cur:", cur, "chars:", chars)
        return res
