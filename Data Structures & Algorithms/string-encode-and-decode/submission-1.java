class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();

        for (String str : strs) {
            sb.append(str.length()).append(",");
        }
        sb.append("#");

        for (int i = 0; i < strs.size(); i++) {
            sb.append(strs.get(i));
        }

        return sb.toString();
    }

    public List<String> decode(String str) {
        ArrayList<String> ans = new ArrayList<>();
        ArrayList<Integer> sizes = new ArrayList<>();

        int i = 0;
        StringBuilder sb = new StringBuilder();
        while (str.charAt(i) != '#') {
            if (str.charAt(i) == ',') {
                sizes.add(Integer.parseInt(sb.toString()));
                sb = new StringBuilder();
            } else {
                sb.append(str.charAt(i));
            }
            i++;
        }
        i++;
        for (int size : sizes) {
            ans.add(str.substring(i, i + size));
            i += size;
        }

        return ans;
    }
}
