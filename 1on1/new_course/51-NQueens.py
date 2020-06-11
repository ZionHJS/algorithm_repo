class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        B = [["." for j in range(n)] for i in range(n)]
        seeds_mid = set()
        seeds_left = set()
        seeds_right = set()
        res = []

        def dfs(cur_i, B):
            nonlocal n, seeds_mid, seeds_left, seeds_right
            if cur_i >= n:
                tmp_res = []
                for row in B:
                    row = "".join(row)
                    tmp_res.append(row)
                res.append(tmp_res)
                return
            for j in range(n):
                if (j not in seeds_mid) and (j-cur_i not in seeds_left) and (j+cur_i not in seeds_right):
                    seeds_mid.add(j)
                    seeds_left.add(j-cur_i)
                    seeds_right.add(j+cur_i)
                    B[cur_i][j] = "Q"
                    dfs(cur_i+1, B)
                    B[cur_i][j] = "."
                    seeds_mid.discard(j)
                    seeds_left.discard(j-cur_i)
                    seeds_right.discard(j+cur_i)
        dfs(0, B)
        return res


class Solution {
    public List < String > wordBreak(String s, List < String > wordDict) {
        HashMap < Integer, List < String >> memo = new HashMap <> ()
        HashSet < String > wordSet = new HashSet <> ()
        for(String word: wordDict) wordSet.add(word)
        dfs(0, wordSet, s, memo)
    }
    private List < String > dfs(int idx, HashSet wordSet, String s, HashMap memo){
        if(idx == s.length()){
            return new ArrayList < String > ()
        }else if(memo.containsKey((Integer)idx)){
            return memo.get((Integer)idx)
        }
        List < String > cur_res = new ArrayList <> ()
        for(int i=idx
            i < s.length()
            i++){
            String tmp_head = s.substring(idx, i+1)
            if(wordSet.contains(tmp_head)){
                List < String > nxt_res = dfs(idx+1, wordSet, s, memo)
                for(String word: nxt_res){
                    String nxt_word = tmp_head + " " + word
                    cur_res.add(word.strip())
                }
            }
        }
        return cur_res
    }
}
