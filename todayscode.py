#Twosum
def twoSum( nums, target):
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
nums=[2,7,11,15]
target=9
print(twoSum(nums,target))
#palindrome
def isPalindrome(x):
    s = str(x)
    if s == s[::-1]:
        return True
    else:
        return False
x=121
print(isPalindrome(x))
#RomantoInteger

def romanToInt(s):
    n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    a = 0
    for i in range(0, len(s) - 1):
        if n[s[i]] < n[s[i + 1]]:
            a -= n[s[i]]
        else:
            a += n[s[i]]
    return a + n[s[-1]]
s="III"
print(romanToInt(s))

#LongestCommonPrefix
 
def longestCommonPrefix(strs):
    sorted_strs = sorted(strs)
    last = sorted_strs[-1]
    first = sorted_strs[0]
    a = ""
    for i in range(min(len(last), len(first))):
        if (first[i] != last[i]):
            return a
        a += first[i]
    return a
strs=["flower","flow","flight"]
print(longestCommonPrefix(strs))
#Remove duplicates
def removeDuplicates(nums):
    nums[:] = set(nums)
    nums.sort()
    return (len(nums))
nums=[1,1,2]
print(removeDuplicates(nums))
#Remove element

def removeElement(nums,val):
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index
nums=[3,2,2,3]
val=3
print(removeElement(nums,val))
#Searchinterst
def searchInsert(nums,target):
    nums.append(target)
    nums.sort()
    for i in nums:
        if i == target:
            x = nums.index(i)
    return x
nums=[1,3,5,6]
target=5
print(searchInsert(nums,target))
#Median of Two sorted Array
def findMedianSortedArrays(nums1,nums2):
    nums1.extend(nums2)
    nums1.sort()
    n = len(nums1)
    if n % 2 == 0:
        x = n // 2
        sum = (nums1[x] + nums1[x - 1]) / 2
        return sum
    else:
        x = n // 2
        sum = nums1[x]
        return sum
nums1 = [1,3]
nums2 = [2]
print(findMedianSortedArrays(nums1,nums2))
#Climbing Stairs
def climbStairs(n):
    a, b, c = 1, 1, 0

    if n <= 1:
        return 1
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
    return c
n=2
print(climbStairs(n))