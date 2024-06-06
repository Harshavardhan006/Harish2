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
#Plus one
def plusOne(digits):
    v = ""
    for i in digits:
        v += str(i)
    x = int(v) + 1
    y = str(x)
    e = []
    for i in y:
        e.append(int(i))
    return e
digits=[1,2,3]
print(plusOne(digits))
#Add Binary
def addBinary(a,b):
    x = int(a, 2)
    y = int(b, 2)
    z = x + y
    q = bin(z)
    return q[2:]
a='11'
b='1'
print(addBinary(a,b)) 
#Sqrt
def mySqrt(x):
    y = math.sqrt(x)
    return (int(y))
x=4
print(mySqrt(x))
#Merge sorted Array
def merge(nums1,m,nums2,n):
    nums1[m:] = nums2
    nums1.sort()
    return nums1
nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
m=3
n=3
print(merge(nums1,m,nums2,n))
#Valid Palindrome
def isPalindrome(s):
    s = [i for i in s.lower() if i.isalnum()]
    return s == s[::-1]
s="race a car"
print(isPalindrome(s))
#Length of last world
def lengthOfLastWord(s):
    x = s.split()
    l = x[-1]
    return (len(l))
s="Hello World"
print(lengthOfLastWord(s))
#Single Number
def singleNumber(nums):
        a = 0
        for i in nums:
            a = a ^ i
        return a
nums=[2,2,1]
print(singleNumber(nums))
#Keyboard Rows
def findWords(words):
    list = []
    s1 = set('qwertyuiop')
    s2 = set('asdfghjkl')
    s3 = set('zxcvbnm')
    for i in words:
        if set(i.lower()).issubset(s1) or set(i.lower()).issubset(s2) or set(i.lower()).issubset(s3):
            list.append(i)
    return list
words=["Hello","Alaska","Dad","Peace"]
print(findWords(words))
#Reverse vowels of string
def reverseVowels(s):
    l = 0
    r = len(s) - 1
    v = "aeiouAEIOU"
    s = list(s)
    while l < r:
        if s[l] not in v:
            l += 1
        if s[r] not in v:
            r -= 1
        if s[l] in v and s[r] in v:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    return ''.join(s)
s="hello"
print(reverseVowels(s)) 

#Power of Two
def isPowerOfTwo(n):
    if n<=0:
        return False
    else:
        return (n&(n-1))==0
n=1
print(isPowerOfTwo(n))

#Add Digits
def addDigits(num):
    if num == 0:
        return 0
    else:
        return 1 + ((num - 1) % 9)
num=38
print(addDigits(num))    

#Reverse string:
def reverseString(s):
    s.reverse()
    return s
s=["h","e","l","l","o"]
print(reverseString(s))

#Contain Duplicates
def containsDuplicate(nums):
    nums.sort()
    n = len(nums)
    for i in range(1, n):
        if nums[i] == nums[i - 1]:
            return True
    return False
nums=[1,2,3,1]
print(containsDuplicate(nums)) 


#Reverse Bits
def reverseBits(n):
    n=int(n,2)
    res = 0
    for i in range(32):
        res = (res << 1)|(n & 1)
        n >>= 1
    return res
n="00000010100101000001111010011100"
print(reverseBits(n))

#Number of 1 bits
def hammingWeight(n):
    count = 0
    while n:
        count += n % 2
        n = n >> 1
    return count
n=11
print(hammingWeight(n)) 















