class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        Sdigit = [str(x) for x in digits]

        number = int("".join(Sdigit))
        Snumber = str(number+1)
        res = []
        for num in Snumber:
            res.append(int(num))

        return res