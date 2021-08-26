#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2021/04/25
# Brief:
#    leetcode
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

"""
1
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
"""

#  示例 1：
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#
#  示例 2：
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#
#  示例 3：
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#
#  提示：
#  2 <= nums.length <= 103
#  -109 <= nums[i] <= 109
#  -109 <= target <= 109
#  只会存在一个有效答案
#
#  Related Topics 数组 哈希表

"""
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
"""

# def twoSum(nums, target):
#     lens = len(nums)
#     j = -1
#     for i in range(lens):
#         if (target-nums[i]) in nums:
#             if (nums.count(target - nums[i]) == 1) & (target - nums[i] == nums[i]):
#                 continue
#             else:
#                 j = nums.index(target - nums[i], i+1)
#                 break
#     if j > 0:
#         return [i, j]
#     else:
#         return []
#
# if __name__ == '__main__':
#     nums = [2, 7, 11, 15]
#     target = 9
#     a = twoSum(nums, target)
#     print(a)

# def twoSum(nums, target):
#     lens = len(nums)
#     j = -1
#     for i in range(1, lens):
#         temp = nums[:i]
#         if (target - nums[i]) in temp:
#             j = temp.index(target - nums[i])
#             break
#     if j >= 0:
#         return [j, i]
#         # return [i, j]
# if __name__ == '__main__':
#     nums = [2, 7, 11, 15]
#     target = 18
#     a = twoSum(nums, target)
#     print a

# def twoSum(nums, target):
#     hashmap = {}
#     for ind,num in enumerate(nums):
#         hashmap[num] = ind
#     for i,num in enumerate(nums):
#         j = hashmap.get(target - num)
#         if j is not None and i!=j:
#             return [i,j]
#
# if __name__ == '__main__':
#     nums = [2, 7, 11, 15]
#     target = 18
#     a = twoSum(nums, target)
#     print a

# def twoSum(nums, target):
#     hashmap = {}
#     for i,num in enumerate(nums):
#         if hashmap.get(target - num) is not None:
#             # return [i, hashmap.get(target-num)]
#             return [hashmap.get(target - num), i]
#         hashmap[num] = i
# if __name__ == '__main__':
#     nums = [2, 7, 11, 15]
#     target = 9
#     a = twoSum(nums, target)
#     print a

"""
2
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""

#  示例 1：
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
#
#  示例 2：
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#
#  示例 3：
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
#
#  提示：
#  每个链表中的节点数在范围 [1, 100] 内
#  0 <= Node.val <= 9
#  题目数据保证列表表示的数字不含前导零
#
#  Related Topics 递归 链表 数学

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
# def addTwoNumbers(l1, l2):
#     n = l1.val + l2.val    # 先计算链表l1和l2中第一位的和，在本实例中就是计算2+5的值
#     l3 = ListNode(n % 10)    # 取余，并将结果赋值给链表l3,类似于C中的指针，即将n%10的值的head给了l3,则此时l3指向了存储数据n%10的位置
#     l3.next = ListNode(n // 10)    #（取整，进位）存储到了l3链表的下一个位置，即n%10的后边，此时l3指向的地址没有发生变化
#     p1 = l1.next    # 将l1链表的下一个值赋值给p1
#     p2 = l2.next    # 将l2链表的下一个值赋值给p2
#     p3 = l3    # 将l3链表中的n%10的值以及位置信息给了p3
#     while True:
#         if p1 and p2:    #判定此时的p1和p2均有值存在
#             sum = p1.val + p2.val + p3.val    # 将sum % 10的值赋值给p3链表的下一个位置，即将之前存储的n//10替换为sum % 10,此时的l3对应位置的值也发生了相同的改变
#             p3.next.val = sum % 10
#             p3.next.next = ListNode(sum // 10)
#             p1 = p1.next
#             p2 = p2.next
#             p3 = p3.next
#         elif p1 and not p2:
#             sum = p1.val + p3.next.val
#             p3.next.val = sum % 10
#             p3.next.next = ListNode(sum // 10)
#             p1 = p1.next
#             p3 = p3.next
#         elif not p1 and p2:
#             sum = p2.val + p3.next.val
#             p3.next.val = sum % 10
#             p3.next.next = ListNode(sum // 10)
#             p2 = p2.next
#             p3 = p3.next
#         else:    # 判定最后一位相加的结果是狗存在进位的情况，当存在进位时，则保留进位值1，在最终返回的结果中将得到体现，即在链表l3(p3)的最后一个节点保留1的值，若不存在进位的情况，此时的0值将要替换为Node，在最终的返回结果中去除该0值
#             if p3.next.val == 0:
#                 p3.next = None
#             break
#     return l3
#
# if __name__ == '__main__':
#     l1 = [2, 4, 3]
#     l2 = [5, 6, 4]
#     a = addTwoNumbers(l1, l2)
#     print a

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         new = ListNode()
#         head = new
#         tail = 0
#         while l1 or l2:
#             new.next = ListNode()
#             new = new.next
#             if l1:
#                 new.val += l1.val
#                 l1 = l1.next
#             if l2:
#                 new.val += l2.val
#                 l2 = l2.next
#             if tail:
#                 new.val = new.val % 10
#         else:
#             if tail:
#                 new.next = ListNode(tail)
#             return head.next
# if __name__ == '__main__':
#     l1 = [2, 4, 3]
#     l2 = [5, 6, 4]
#     a = Solution(l1)
#     print a

"""
3
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。 
"""

#  示例 1:
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#  示例 2:
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#  示例 3:
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#  示例 4:
# 输入: s = ""
# 输出: 0
#
#  提示：
#  0 <= s.length <= 5 * 104
#  s 由英文字母、数字、符号和空格组成
#  Related Topics 哈希表 双指针 字符串 Sliding Window

# def finstr(findstr:str):
#     for i in range(findstr):
#         for j in range(len(findstr)):
#             data = findstr[0:1]
#             if str(findstr[j]) in str(data):
#                 m = findstr[0:i]
#             else:
#                 m = findstr[0:j+1]
#     return len(m)
#
# # 测试
# from sixexapmle import finstr
# import  unittest
# class Test(unittest.TestCase):
#     def setUp(self) -> None:pass
#     def tearDown(self) -> None:pass
#     def testone(self):
#         reslut=finstr("0")
#         self.assertEqual(1,reslut)
#     def testtewo(self):
#         reslut=finstr("01")
#         self.assertEqual(2,reslut)
#     def testthree(self):
#         reslut=finstr("011")
#         self.assertEqual(2,reslut)
# if __name__=="__main__":
#     unittest.main()

# class Solution:
#     def lengthOfLongestSubstring(self, s:str) -> int:
#         L = len(s)
#         if L < 2:
#             return L
#         head = 0
#         tail = 1
#         cnt = 1    # 设置初始窗口大小为1
#         while tail < L:
#             while tail < L and s[tail] not in s[head:tail]:
#                 tail += 1
#             cnt = max(cnt, tail-head)
#             if tail != L:
#                 head += s[head:tail].index(s[tail])+1    # 计算头指针的移动步数
#         return cnt
#
# if __name__ == '__main__':
#     a = Solution
#     print a

"""
4
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数
"""
#
#  示例 1：
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#
#  示例 2：
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#
#  示例 3：
# 输入：nums1 = [0,0], nums2 = [0,0]
# 输出：0.00000
#
#  示例 4：
# 输入：nums1 = [], nums2 = [1]
# 输出：1.00000
#
#  示例 5：
# 输入：nums1 = [2], nums2 = []
# 输出：2.00000
#
#  提示：
#  nums1.length == m
#  nums2.length == n
#  0 <= m <= 1000
#  0 <= n <= 1000
#  1 <= m + n <= 2000
#  -106 <= nums1[i], nums2[i] <= 106
#
#  进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
#  Related Topics 数组 二分查找 分治算法

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         def getKthElement(k):
#             index1, index2 = 0, 0
#             while True:
#                 # 特殊情况
#                 if index1 == m:
#                     return nums2[index2 + k -1]
#                 if index2 == n:
#                     return nums1[index1 + k -1]
#                 if k == 1:
#                     return min(nums1[index1], nums2[index2])
#
#                 # 正常情况
#                 newIndex1 = min(index1 + k // 2 - 1, m -1)
#                 newIndex2 = min(index2 + k // 2 - 1, n -1)
#                 pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
#                 if pivot1 <= pivot2:
#                     k -= newIndex1 - index1 + 1
#                     index1 = newIndex1 + 1
#                 else:
#                     k -= newIndex2 - index2 + 1
#                     index2 = newIndex2 + 1
#         m, n = len(nums1), len(nums2)
#         totalLength = m + n
#         if totalLength % 2 == 1:
#             return getKthElement((totalLength + 1) // 2)
#         else:
#             return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 +1)) / 2
#
# if __name__ == '__main__':
#     nums1 = [1, 3]
#     nums2 = [2]
#     a = Solution.findMedianSortedArrays(self=Solution, nums1, nums2)
#     print a

"""
5
给你一个字符串 s，找到 s 中最长的回文子串。
"""
#
#  示例 1：
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#
#  示例 2：
# 输入：s = "cbbd"
# 输出："bb"
#
#  示例 3：
# 输入：s = "a"
# 输出："a"
#
#  示例 4：
# 输入：s = "ac"
# 输出："a"
#
#  提示：
#  1 <= s.length <= 1000
#  s 仅由数字和英文字母（大写和/或小写）组成
#
#  Related Topics 字符串 动态规划

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         if n < 2:
#             return s
#
#         max_len = 1
#         begin = 0
#         # dp[i][j] 表示 s[i..j] 是否是回文串
#         dp = [[False] * n for _ in range(n)]
#         for i in range(n):
#             dp[i][i] = True
#
#         # 递推开始
#         # 先枚举子串长度
#         for L in range(2, n + 1):
#             # 枚举左边界，左边界的上限设置可以宽松一些
#             for i in range(n):
#                 # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
#                 j = L + i - 1
#                 # 如果右边界越界，就可以退出当前循环
#                 if j >= n:
#                     break
#
#                 if s[i] != s[j]:
#                     dp[i][j] = False
#                 else:
#                     if j - i < 3:
#                         dp[i][j] = True
#                     else:
#                         dp[i][j] = dp[i + 1][j - 1]
#
#                 # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
#                 if dp[i][j] and j - i + 1 > max_len:
#                     max_len = j - i + 1
#                     begin = i
#         return s[begin:begin + max_len]

