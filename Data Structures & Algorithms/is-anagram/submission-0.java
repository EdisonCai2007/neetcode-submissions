class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> freq = new HashMap<>();

        if (s.length() != t.length()) return false;

        for (int i = 0; i < s.length(); i++) {
            freq.put(s.charAt(i), freq.getOrDefault(s.charAt(i),0)+1);
        }

        for (int i = 0; i < t.length(); i++) {
            if (freq.containsKey(t.charAt(i)) && freq.get(t.charAt(i)) > 0) {
                freq.put(t.charAt(i),freq.get(t.charAt(i))-1);
            } else {
                return false;
            }
        }

        return true;
    }
}
