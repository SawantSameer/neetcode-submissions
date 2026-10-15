class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        s= ''
        while i<len(chars):
            s+=chars[i]
            j = i+1
            while j<len(chars) and chars[j]==chars[i]:
                j+=1

            if j-i>1:
                s += str(j-i)
            i = j

        k = 0
        while k<len(s):
            chars[k] = s[k]
            k+=1

        return k
        
