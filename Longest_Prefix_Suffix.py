class Solution:
    def lps(self, s):
        n = len(s)
        lps_array = [0] * n
        length = 0
        i = 1

        
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps_array[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps_array[length - 1]
                else:
                    lps_array[i] = 0
                    i += 1

        return lps_array[-1]
