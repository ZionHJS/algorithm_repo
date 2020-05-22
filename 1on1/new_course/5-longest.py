

class Solution {
    public String longestPalindrome(String s) {
        if(s.length() == 0) return ""
        boolean[][] dp = new boolean[s.length()][s.length()]
        String ans = s.substring(0, 1)
        for(int i=s.length()-2
            i > -1
            i--){
            for(int j=i
                j < s.length()
                j++){
                if(i == j){
                    dp[i][j] = true
                    continue
                }
                if(s.charAt(i) == s.charAt(j)){
                    if((j-i < 2) | | (dp[i+1][j-1] == true)){
                        dp[i][j] = true
                        if((j-i+1) > ans.length()){
                            ans = s.substring(i, j+1)
                        }
                    }
                }
            }
        }
        return ans
    }
}
