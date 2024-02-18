class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        a = max(candies)
        b = []
        for c in candies:
            if c + extraCandies >= a :
                b.append(True)
            else:
                b.append(False)
        return b