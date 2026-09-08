class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"

        for _ in range(n - 1):
            ans = ""
            i = 0

            while i < len(s):
                count = 1

                while i < len(s) - 1 and s[i] == s[i + 1]:
                    count += 1
                    i += 1

                ans += str(count)
                ans += s[i]
                i += 1

            s = ans

        return s