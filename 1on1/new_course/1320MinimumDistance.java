class Solution {
    public int minimumDistance(String word) {
        String chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        HashMap<Character, Pos> board = new HashMap<>();
        for (int i = 0; i < chars.length(); i++) {
            Integer dvd = i / 6;
            Integer rem = i % 6;
            Pos curPos = new Pos(dvd, rem);
            board.put(chars.charAt(i), Pos);
        }
        System.out.println("board:" + board.toString());

        Status start = new Status();
        HashMap<Status, Integer> dp = new HashSet<>();
        dp.put(start, 0);

        for (Character c : word.toCharArray()) {
            HashSet<Status> nxtdp = new HashSet<>();
            for (Status status : dp) {
                // for left-finger
                nxtStatusl = new Status(status.left, status.right);
                nxtStatusl.left = c;
                Integer disl = getDis(status.left, c, board);
                if (nxtdp.get(nxtStatusl) != null) {
                    disl = Math.min(nxtdp.get(nxtStatusl), disl);
                }
                nxtdp.put(nxtStatusl, disl);
                // for right-finger
                nxtStatusr = new Status(status.left, status.right);
                nxtStatus.right = c;
                Integer disr = getDis(status.right, c, board);
                if (nxtdp.get(nxtStatus) != null) {
                    disr = Math.min(nxtdp.get(nxtStatus), disr);
                }
                nxtdp.put(nxtStatus, disr);
            }
            dp = nxtdp;
        }
        return Math.min(dp.values());
    }

    private Integer getDis(Character c1, Character c2, HashMap board) {
        if (c1 == null || c2 == null)
            return 0;
        Pos pos1 = board.get(c1);
        Pos pos2 = board.get(c2);
        return abs(pos1.row - pos2.row) + abs(pos1.col - pos2.col);
    }
}

class Pos {
    Integer row;
    Integer col;

    public void Pos(Integer r, Integer c) {
        this.row = r;
        this.col = c;
    }
}

class Status {
    Character left;
    Character right;

    public void Status() {
    }

    public void Status(Character l, Character r) {
        this.left = l;
        this.right = r;
    }
}