class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
          const complementDictionary = {};
  for (let i = 0; i < nums.length; i++) {
    complementDictionary[target - nums[i]] = i;
  }

  console.log(complementDictionary);

  for (let i = 0; i < nums.length; i++) {
    if (complementDictionary[nums[i]] !== undefined && i !== complementDictionary[nums[i]]) {
      return [i, complementDictionary[nums[i]]];
    }
  }
    }
}
