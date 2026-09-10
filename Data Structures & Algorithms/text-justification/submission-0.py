class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        i = 0

        while i<len(words):
            if length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1
            else:
                #Line comlete
                extraSpace = maxWidth - length
                rem = extraSpace % max(1, len(line)-1)
                space = extraSpace//max(1, len(line)-1)

                for j in range(max(1, len(line)-1)):
                    line[j] += " "*space
                    if rem:
                        line[j] += " "
                        rem -=1

                res.append("".join(line))
                line, length = [], 0

        # Handaling last line
        lastLine = " ".join(line)
        trailSpace = maxWidth - len(lastLine)
        res.append(lastLine + " "*trailSpace)
        return res