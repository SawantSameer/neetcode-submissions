class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0]*n

        for i in range(n):
            j = 0
            total = 0
            while j<n:
                if i==j:
                    j+=1
                    continue
                if boxes[j]=='1':
                    total+=abs(j-i)
                j+=1

            answer[i]=total

        return answer
