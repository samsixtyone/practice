
class Solution:
  def pivotIndex(self, nums):
    totalSum = sum(nums)
    leftSum = 0

    for i, num in enumerate(nums):
      if leftSum == (totalSum - leftSum - num):
        return i
      leftSum += num
    return -1 

if __name__ == "__main__":
  solution = Solution()
  print (solution.pivotIndex([1,2,3,4,3,2,1]))
  print (solution.pivotIndex([1,100,50,-51,1,1]))
