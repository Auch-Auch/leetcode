import random


class Solution:
    def search(self, nums: list, target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
        return -1

    def mySqrt(self, x: int) -> int:
        return int(x**0.5)

    def guessNumber(self, n: int) -> int:
        left = 0
        right = n
        middle = (left + right) // 2
        guessNum = guess(middle)
        while guessNum != 0:
            if guessNum == -1:
                right = middle - 1
            elif guessNum == 1:
                left = middle + 1
            middle = (left + right) // 2
            guessNum = guess(middle)
        return middle

    def get_pi(self, n):
        area = 0
        total_area = 0
        for _ in range(n):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            distance = x**2 + y**2
            if distance <= 1:
                area += 1
            total_area += 1
        return 4 * area/total_area

    def first_bad_varsion(self, n):
        left, right = 1, n
        while left < right:
            mid = (left + right) / 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return int(left)
