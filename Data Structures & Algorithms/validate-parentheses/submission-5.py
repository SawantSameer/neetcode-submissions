class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False

        stack = []
        
        for bracket in s:
            if bracket in ["(", "{", "["]:
                stack.append(bracket)

            else:
                if stack:
                    if bracket == ")":
                        if stack.pop()!="(":
                            return False
                    elif bracket == "}":
                        if stack.pop()!="{":
                            return False
                    else:
                        if stack.pop()!="[":
                            return False
                else:
                    return False

        return len(stack)==0