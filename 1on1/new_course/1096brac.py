import itertools


class Solution:
    def braceExpansionII(self, E: str) -> List[str]:
        stack = [[]]
        chars = ""
        pros = [""]
        tmp = []
        for i in range(len(E)):
            if E[i] == "{":
                if i > 1 and E[i-1] != ",":
                    prev_pro = pros.pop()
                    product = ["".join(c) for c in itertools.product(
                        prev_pro, [chars])] if chars else prev_pro
                    pros.append(product)
                    tmp = []
                    chars = ""
                else:
                    pop = stack.pop()
                    pop += tmp
                    stack.append(pop)
                    pros.append(chars)
                    tmp = []
                    chars = ""
                    #print("stack:", stack)
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

                #prev = stack.pop()
                #cur = list(set(prev+ product))
                if i+1 < len(E):
                    if E[i+1] == ",":
                        tmp = stack.pop()+product
                        chars = ""
                    else:
                        pros.append(product)
                        tmp = []
                        chars = ""
                else:
                    tmp = stack.pop()+product
                    chars = ""

                #print("tmp:", tmp)
                # stack.append(tmp)

        #print("tmp:", tmp, "res:", list(set(tmp)))
        #res = list(set(tmp)) if not chars else list(set(tmp.append(chars)))
        # res.sort()
        return tmp
