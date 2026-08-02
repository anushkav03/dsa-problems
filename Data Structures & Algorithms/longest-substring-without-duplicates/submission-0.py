class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        right = 0
        left = 0
        window = {s[0]} #hash set with first elem
        longest = 0

        while right < len(s) - 1:
            right += 1
            if s[right] not in window:
                window.add(s[right])
            else:
                # window has duplicates
                while s[left] != s[right]:
                    window.remove(s[left])
                    left += 1
                window.remove(s[left])
                left += 1
                window.add(s[right])
            longest = max(longest, len(window))
        return longest