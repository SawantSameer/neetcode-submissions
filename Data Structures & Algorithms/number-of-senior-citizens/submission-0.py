class Solution:
    def countSeniors(self, details: List[str]) -> int:
        numOfPass = 0
        for detail in details:

            if int(detail[11:13])>60:
                numOfPass+=1

        return numOfPass