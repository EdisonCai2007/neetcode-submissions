class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (Character.isLetterOrDigit(s.charAt(i))) sb.append(s.charAt(i));
        }
        
        String s2 = sb.toString().toLowerCase();
        for (int i = 0; i < s2.length()/2; i++) {
            if (s2.charAt(i) != s2.charAt(s2.length()-i-1)) {
                return false;
            }
        }

        return true;
    }
}
