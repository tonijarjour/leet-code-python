class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = [c.lower() for c in s if c.isalnum()]
        return clean == [c for c in reversed(clean)]


s = Solution()
s.isPalindrome("A man, a plan, a canal: Panama")
