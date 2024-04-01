#Kids with greatest number of candies
def kidsWithCandies(candies,extraCandies):
    res = []
    for i in candies:
        if (i + extraCandies) >= max(candies):
            res.append(True)
        else:
            res.append(False)
    return res
candies=[2,3,5,3,1]
extraCandies=3
print(kidsWithCandies(candies,extraCandies))

#Single Number
def singleNumber(nums):
    a = 0
    for i in nums:
        a = a ^ i
    return a
n=[2,2,1]
print(singleNumber(n))

#Can Place Flowers
def canPlaceFlowers(flowerbed, n):
    a = 0
    flowerbed.insert(0, 0)
    flowerbed.append(0)
    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i] == 0 and flowerbed[i + 1] and flowerbed[i - 1] == 0:
            flowerbed[i] = 1
            a = n - 1
    return a <= 0
flowerbed=[1,0,0,0,1]
n=1
print(canPlaceFlowers(flowerbed,n)) 

#Greatest common Divisor of Strings:
from math import gcd
def gcdOfStrings(str1,str2):
    if str1 + str2 != str2 + str1:
        return ""
    maxlength = gcd(len(str1), len(str2))
    return str1[:maxlength]
str1="ABCABC"
str2="ABC"
print(gcdOfStrings(str1,str2))