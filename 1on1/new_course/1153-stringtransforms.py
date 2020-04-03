import collections
import copy


class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        dic1 = collections.defaultdict(lambda: [])
        for i in range(len(str1)):
            dic1[str1[i]].append(i)  # char => [idx1, idx2...]

        # dfs()
        self.ans = False

        def dfs(cur_str1, str2, cur_dic1):
            if cur_str1 == str2:
                self.ans = True
                return

            for key in cur_dic1:
                if str2[cur_dic1[key][0]] != key:
                    new_str1 = cur_str1
                    for idx in cur_dic1[key]:
                        new_str1 = new_str1[:idx] + \
                            str2[cur_dic1[key][0]] + new_str1[idx+1:]
                    dic2 = collections.defaultdict(lambda: [])
                    # print("newkey:", str2[cur_dic1[key][0]])
                    # print("cur_dic1[str2[cur_dic1[key][0]]]:", cur_dic1[str2[cur_dic1[key][0]]])
                    # print("cur_dic1[key]:", cur_dic1[key])
                    # print("combine:", cur_dic1[str2[cur_dic1[key][0]]] + cur_dic1[key])
                    dic2[str2[cur_dic1[key][0]]
                         ] = cur_dic1[str2[cur_dic1[key][0]]] + cur_dic1[key]
                    #new_dic1 = {**cur_dic1, **dic2}
                    new_dic1 = copy.deepcopy(cur_dic1)
                    new_dic1.update(dic2)
                    del new_dic1[key]
                    dfs(new_str1, str2, new_dic1)

        dfs(str1, str2, dic1)

        return self.ans
