class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const dictionary = {};

  for (let i = 0; i < nums.length; i++) {
    const element = nums[i];
    if (dictionary[element] !== undefined) {
      dictionary[element] += 1;
    } else {
      dictionary[element] = 1;
    }
  }

  for (const value of Object.values(dictionary)) {
    if (value > 1) {
      return true;
    }
  }

  return false;
    }
}
