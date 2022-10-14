class solution:
  def SumOfArray(nums: List[int]) -> int:
    # Time Complexity: O(n)
    ans = 0
    for x in nums:
      ans+=x
    return ans
