class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        #if (sum (flowerbed) + n) > (len(flowerbed)//sum(flowerbed)):
        #    return False
        e = 0
        j = 0
        for i in flowerbed:
            if j == 0:
                 if len(flowerbed) == 1 and flowerbed[j] == 0:
                    flowerbed[j] = 1
                    e+=1                    
                    j+=1
                 elif flowerbed[j] == 0 and flowerbed[j+1] == 0:
                    flowerbed[j] = 1
                    e+=1
                    j+=1
                 else:
                    j+=1
            if j == (len (flowerbed) -1):
                if flowerbed[j-1] == 0 and flowerbed[j] == 0:
                    flowerbed[j] = 1
                    e+=1
                else:
                    continue
            else:
                    if flowerbed[j-1] == 0 and flowerbed[j+1] == 0 and flowerbed[j] == 0:
                        flowerbed[j] = 1
                        e+=1
            j += 1
        if e < n:
            return False
        else:
            return True