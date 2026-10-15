class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        s= ''
        while i<len(chars):
            s+=chars[i]
            j = i+1
            count = 1
            while j<len(chars):
                if chars[j]==chars[i]:
                    count+=1
                else:
                    break
                j+=1
            if count>1:
                digit = ''
                while count>0:
                    digit = str(count%10)+digit
                    count = count//10
                s += digit
            i = j
        k = 0
        for char in s:
            chars.insert(k, char)
            k+=1

        return len(s)
        
