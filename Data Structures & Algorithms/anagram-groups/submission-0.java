class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagrams = new HashMap<>();

        for (int i = 0; i < strs.length; i++) {
            String word = strs[i];

            int[] freq = new int[26];

            for (int j = 0; j < word.length(); j++) {
                freq[word.charAt(j) - 'a']++;
            }

            StringBuilder sb = new StringBuilder();
            for (int num : freq) {
                sb.append(num).append("#");
            }

            String key = sb.toString();
            if (!anagrams.containsKey(key)) {
                anagrams.put(key, new ArrayList<String>());
            }
            anagrams.get(key).add(word);
        }

        return new ArrayList<>(anagrams.values());
    }
}
